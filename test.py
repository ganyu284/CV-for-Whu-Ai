from logger import My_logger
from Argparse import Arg_parse
def test_logger():
    parser = Arg_parse().parser
    args = parser.parse_args()
    Log = My_logger(args.logger_config).logger
    Log.debug = ("This is a debug message")
    Log.info("This is a info message")
    Log.warning("This is a warn message")
    Log.error("This is a error message")
    Log.critical("This is a critical message")

if __name__=='__main__':
    test_logger()