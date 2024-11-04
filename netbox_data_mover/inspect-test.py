import inspect
import importlib
import pprint

print("Starting Up")
module_name = 'pyVmomi'
class_name = 'vim'

print(f"Importint Module {module_name}")
lib_module = importlib.import_module(module_name)
print(f"Looking for module {class_name}")
class_obj = getattr(lib_module, class_name, None)

if class_obj is None:
    print(f'Class {class_name} not found in module {module_name}.')

 # Get all subclasses of the class
subclasses = [subclass.__name__ for subclass in class_obj.__subclasses__()]

# Get all callable methods of the class (excluding special/magic methods)
methods = [
    name for name, member in inspect.getmembers(class_obj)
    if inspect.isfunction(member) or inspect.ismethod(member)
    and not name.startswith('__')
]

response_data = {
    'class_name': class_name,
    'subclasses': subclasses,
    'methods': methods
    }

pprint.pp(response_data)
