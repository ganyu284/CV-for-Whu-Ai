from logger import My_logger
import importlib 
log_register = My_logger().logger

MODEL_MODULES = ["dataloader"]
ALL_MODULES = [("dataset", MODEL_MODULES)]

class Register:

    def __init__(self,registry_name):
        self._dict = {}
        self._name = registry_name
    
    def __setitem__(self,key,value):
        if not callable(value):
            raise Exception(f"Value of a Registry must be callable!\nValue:{value}")
        if key is None:
            key = value.__name__
        if key in self._dict:
            log_register.warning(f"Key {key} already in registry {self._name}")
        self._dict[key] = value

    def register(self, target):

        def add(key, value):
            self[key] = value
            return value
        
        if callable(target):
            return add(None, target)
        
        return lambda x: add(target,x)
    
    def __getitem__(self, key):
        return self._dict[key]

    def __contains__(self, key):
        return key in self._dict

    def keys(self):
        return self._dict.keys()
    
class Registers:
        
    def __init__(self):
        raise RuntimeError("Registeries is not intended to be instantiated")
        
    dataloader = Register('dataloader')

def _handle_errors(errors):
    
    if not errors:
        return
    
    for name,err in errors:
        log_register.warning("Module {} import failed: {}",format(name,err))

def import_all_modules_for_register(custom_module_paths = None):
    Modules = []
    errors = []
    for base_dir, modules in ALL_MODULES:
        for name in modules:
            full_name = base_dir + "." +name
            Modules.append(full_name)
    if isinstance(custom_module_paths, list):
        Modules += custom_module_paths
    
    for module in Modules:
        try:
            importlib.import_module(module)
        except ImportError as error:
            errors.append((module, error))
    _handle_errors(errors)


