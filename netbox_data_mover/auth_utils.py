import importlib

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
