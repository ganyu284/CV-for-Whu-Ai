import os
import logging
import time
import yaml
import sys
from time import strftime
class My_logger(object):
    #''' set logger for the whole repo
    #       func:
    #            -get_file_handler: set the handler to file
    #            -get_console_handle: set the handler to console
    # '''
    def __init__(self, logger_args_path = None):
        #''' initial args for logger,all the args will be saved in a yaml,
        # and you can find it through the path
        #    args:
        #         - loggar_args_path:   the path for yaml
        # '''
        if logger_args_path is None:
            logger_args_path = "config/logger/letnet5.yaml"
        if os.path.exists(logger_args_path):
            with open(logger_args_path, 'r', encoding = 'utf_8') as f:
                config = yaml.load(stream = f, Loader = yaml.FullLoader)
        self.FMT = config['FMT']
        self.DATEFMT = config['DATEFMT']
        self.LOGGER_FILE_PATH = config['LOGGER_FILE_PATH']
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter(fmt = self.FMT, datefmt =self.DATEFMT)
        self.logger_file = '{0}{1}.log'.format(self.LOGGER_FILE_PATH,strftime("%Y-%m-%d"))
        self.logger.addHandler(self.get_file_handle(self.logger_file))
        self.logger.addHandler(self.get_console_handle())
        self.logger.setLevel(eval('logging.DEBUG'))
    def get_file_handle(self, file_name):
        file_handle = logging.FileHandler(file_name, encoding = 'utf_8')
        file_handle.setFormatter(self.formatter)
        return file_handle
    def get_console_handle(self): 
        console_handle = logging.StreamHandler(sys.stdout)
        console_handle.setFormatter(self.formatter)
        return console_handle