import inspect
import importlib

# Get the datasource ID and find the corresponding DataMoverDataSource instance
try:
    module_name = 'pynetbox'
    class_name = 'api'

    # Import the module and get the class specified by auth_function
    lib_module = importlib.import_module(module_name)
    class_obj = getattr(lib_module, class_name, None)

    if class_obj is None:
        print(f'Class {class_name} not found in module {module_name}.')

    # Get all attributes and methods of the class
    attributes = [attr for attr, _ in inspect.getmembers(class_obj)]
    response_data = {
        'class_name': class_name,
        'attributes': attributes
    }
except ModuleNotFoundError:
    print(f'Module {module_name} not found.')