import ssl
import importlib
import datetime
import inspect
import types
from .models import DataMoverDataSource
import ast

class APIDataSource:
    def __init__(self, datasource_instance: DataMoverDataSource):
        # Assign properties directly from the model instance
        self.name = datasource_instance.name
        self.api = None
        self.clients = []
        self.session_expiry = {}
        
        # Extract fields from datasource_instance and assign them
        self.base_urls = datasource_instance.base_urls.split(",") if datasource_instance.base_urls else []
        self.auth_method = datasource_instance.auth_method
        self.auth_function = datasource_instance.auth_function
        self.module = datasource_instance.module
        self.auth_args = datasource_instance.auth_args
        self.fetch_function = datasource_instance.fetch_function

    def is_session_valid(self, base_url):
        if base_url in self.session_expiry:
            return datetime.datetime.now() < self.session_expiry[base_url]
        return False

    def prepare_auth_args(self):
        """Prepare auth args, converting lists to dicts as needed and setting SSL context."""
        auth_args = self.auth_args

        # Convert auth_args list to dictionary if necessary
        if isinstance(auth_args, list):
            auth_args = {arg['name']: arg['value'] for arg in auth_args}

        # Handle SSL context if specified
        if auth_args.get('sslContext') == 'ignore':
            auth_args['sslContext'] = ssl._create_unverified_context()
        elif auth_args.get('sslContext') == 'None':
            auth_args['sslContext'] = None
        return auth_args

    def get_auth_function(self, module, function_path):
        """Retrieve auth function from a module, allowing for submodules."""
        func_parts = function_path.split(".")
        if len(func_parts) == 1:
            return getattr(module, func_parts[0])
        else:
            submodule = importlib.import_module(f"{module.__name__}.{func_parts[0]}")
            return getattr(submodule, func_parts[1])

    def authenticate(self):
        """Handle authentication, supporting both Swagger and non-Swagger clients."""
        for base_url in self.base_urls:
            module = importlib.import_module(self.module)
            auth_method = self.auth_method
            auth_func = self.get_auth_function(module, self.auth_function)
            auth_args = self.prepare_auth_args()
            
            # Add base_url if required
            if 'base_url' in inspect.signature(auth_func).parameters:
                auth_args['base_url'] = base_url
                
            if not (self.api and self.is_session_valid(base_url)):
                # Handle authentication methods
                if auth_method == 'token':
                    self.api = auth_func(base_url, token=self.auth_args.get('token'))
                    if base_url not in self.session_expiry: 
                        self.clients.append(self.api)
                    self.session_expiry[base_url] = datetime.datetime.now() + datetime.timedelta(minutes=2)
                elif auth_method == 'login':
                    if auth_args:
                        self.api = auth_func(**auth_args)
                        if base_url not in self.session_expiry: 
                            self.clients.append(self.api)
                        self.session_expiry[base_url] = datetime.datetime.now() + datetime.timedelta(minutes=2)
                    else:
                        raise ValueError("Login-based authentication requires auth_args to be set.")
    

    def fetch_data(self, api_client):
        """
        Fetch data from the API using either a direct fetch_function from the client
        or custom Python code. Handles dynamically loaded functions.
        """
        fetch_function = self.fetch_function

        # Determine if the fetch function needs to be evaluated
        if isinstance(fetch_function, str):
            try:
                # Parse the string to see if it's valid Python code or a direct function reference
                parsed_code = ast.parse(fetch_function, mode='eval')
                is_code = False
            except SyntaxError:
                # If it's not valid as a Python expression, it could be a block of Python code
                is_code = True

            if is_code:
                # Execute custom Python code
                local_vars = {'api_client': api_client}
                try:
                    exec(fetch_function, globals(), local_vars)
                    if 'fetch_data' not in local_vars:
                        raise ValueError("The custom code must define a function named 'fetch_data(api_client)'")
                    fetch_func = local_vars['fetch_data']
                except Exception as e:
                    raise RuntimeError(f"Error executing custom Python code: {str(e)}")

            else:
                # It's a reference to a function, resolve it
                try:
                    fetch_func = eval(compile(parsed_code, filename="<ast>", mode='eval'))
                except Exception as e:
                    raise RuntimeError(f"Error evaluating fetch function: {str(e)}")
                
                if not callable(fetch_func):
                    raise ValueError("The evaluated fetch function is not callable.")

        elif callable(fetch_function):
            # When fetch_function is already callable
            fetch_func = fetch_function

        else:
            raise ValueError("fetch_function must be either a callable or a string representing Python code.")

        # Use the fetch_func to get the data
        if isinstance(fetch_func, types.FunctionType):
            return fetch_func(api_client)
        else:
            raise TypeError("fetch_data is not a valid function")
