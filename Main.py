import torch
import torch.nn as nn
from logger import My_logger
from Argparse import Arg_parse
from register import import_all_modules_for_register
def main():
    import_all_modules_for_register()
    Log = My_logger().logger
    Log.info('the program is running')
if __name__ =="__main__":
    main()