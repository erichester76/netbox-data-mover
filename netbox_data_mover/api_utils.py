import ssl
import importlib
from .models import DataMoverDataSource
import requests
import datetime
import inspect
import types

class APIDataSource(DataMoverDataSource):
    def __init__(self, name):
        self.name = name
        self.api = None
        self.clients = []
        self.session_expiry = {}
        
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

    def get_nested_function(self, api_client, function_path):
        """
        Recursively get a function from the API client.
        
        :param api_client: The API client (e.g., NetBox client)
        :param function_path: Path to the function (e.g., 'dcim.device_types.filter')
        :return: The function object
        """
        parts = function_path.split('.')
        func = api_client  # Start with the root client (e.g., pynetbox.NetBox())

        # Traverse down the client object tree
        for part in parts:
            try:
                func = getattr(func, part)
            except AttributeError:
                raise AttributeError(f"Attribute '{part}' not found in API client at path '{function_path}'")
        
        # Ensure the final attribute is callable
        if not callable(func):
            raise TypeError(f"Final attribute in path '{function_path}' is not callable.")
        
        return func

    def get_nested_attr(self, obj, attrs):
        """
        Recursively get attributes from an object based on a list of attribute names.
        Handles attributes like 'runtime.powerState' from YAML.
        """
        for attr in attrs:
            obj = getattr(obj, attr, None)
            if obj is None:
                break  # Stop if any attribute in the chain is None
        return obj


    def authenticate(self):
        """Handle authentication, supporting both Swagger and non-Swagger clients."""
        for base_url in self.base_urls:
            module = importlib.import_module(self.module)
            auth_method = self.auth_method
            auth_func = self.get_auth_function(module, self.auth_function)
            auth_args = self.prepare_auth_args(base_url)
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
        Fetch data from the API using either a direct fetch_data_function or a custom Python code block.
        Dynamically load modules specified in the 'imports' section of the YAML and inject into globals.
        """

        # Handle imports specified in YAML
        local_vars = {'api_client': api_client}

        # Fetch custom Python code to execute
        fetch_data_code = self.fetch_function

        if fetch_data_code:
            print(f"Using custom Python code for data fetch")

            # Execute the provided code within the local scope, passing in local_vars to exec
            exec(fetch_data_code, globals(), local_vars)

            # Ensure the 'fetch_data' function is defined in the code
            if 'fetch_data' not in local_vars:
                raise ValueError("The custom code must define a function 'fetch_data(api_client)'")

            # Call the dynamically defined function
            fetch_func = local_vars['fetch_data']
            if isinstance(fetch_func, types.FunctionType):
                return fetch_func(api_client)
            else:
                raise TypeError("fetch_data is not a valid function")

        # If no fetch method is specified, raise an error
        raise ValueError("No valid fetch method (fetch_data_function or fetch_data_code) found")

        
   