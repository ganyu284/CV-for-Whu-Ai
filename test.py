from logger import My_logger
from Argparse import Arg_parse
from register import Registers
from register import import_all_modules_for_register
def test_logger():
    parser = Arg_parse().parser
    args = parser.parse_args()
    Log = My_logger(args.logger_config).logger
    Log.debug = ("This is a debug message")
    Log.info("This is a info message")
    Log.warning("This is a warn message")
    Log.error("This is a error message")
    Log.critical("This is a critical message")

def test_register():
    print(f"Register.model._dict before: {str(Registers.dataloader._dict)}")
    import_all_modules_for_register()
    print(f"Register.model._dict after: {str(Registers.dataloader._dict)}")   
    Registers.dataloader["Minstdataloader"].output()
if __name__=='__main__':
    test_register()