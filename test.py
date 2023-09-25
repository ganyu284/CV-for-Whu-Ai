from logger import My_logger

def test_logger():
    Log = My_logger().logger
    Log.debug = ("This is a debug message")
    Log.info("This is a info message")
    Log.warning("This is a warn message")
    Log.error("This is a error message")
    Log.critical("This is a critical message")

if __name__=='__main__':
    test_logger()