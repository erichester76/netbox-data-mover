import importlib
import ast
import types

class DataSourceAuth:
    @staticmethod
    def authenticate(datasource):
        """
        Authenticate to the data source using the provided auth details.
        
        Args:
            datasource (DataMoverDataSource): The datasource configuration.

        Returns:
            client: Authenticated client instance for the data source.
        """
        try:
            # Dynamically import the module
            module_name = datasource.module
            auth_function_name = datasource.auth_function
            auth_args = datasource.auth_args

            module = importlib.import_module(module_name)

            # Get the authentication function
            auth_function = getattr(module, auth_function_name, None)
            if auth_function is None:
                raise ImportError(f'Auth function "{auth_function_name}" not found in module "{module_name}".')

            # Use the provided arguments to authenticate
            client = auth_function(**auth_args)
            return client

        except ModuleNotFoundError:
            raise ImportError(f'Module "{module_name}" not found.')
        except Exception as e:
            raise RuntimeError(f'Failed to authenticate: {str(e)}')

    @staticmethod
    def fetch_data(datasource, client, endpoint):
        """
        Fetch data using the provided data source details and the authenticated client.

        Args:
            datasource (DataMoverDataSource): The datasource configuration.
            client: The authenticated client instance.

        Returns:
            data: Retrieved data from the data source.
        """
        try:
            fetch_function = None
            # Determine whether the fetch function needs to be evaluated
            fetch_function_code = datasource.fetch_function

            if datasource.fetch_function_should_eval:
                # Safely parse the string into Python code if it should be evaluated
                try:
                    parsed_code = ast.parse(fetch_function_code, mode='eval')
                    fetch_function = eval(compile(parsed_code, filename="<ast>", mode='eval'))
                except Exception as e:
                    raise RuntimeError(f"Error evaluating fetch_function: {str(e)}")
                
                if not callable(fetch_function):
                    raise ValueError("Evaluated fetch_function is not callable.")
            
            # Assuming the fetch function takes a client and an endpoint as arguments
            return fetch_function(client, datasource.base_urls[0], endpoint, 1)

        except Exception as e:
            raise RuntimeError(f'Failed to fetch data: {str(e)}')
