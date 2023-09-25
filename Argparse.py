import argparse

class Arg_parse(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = 'args needed by traing or testing')
        self.parser.add_argument('--logger_config', type = str, default = None, help = 'where is the logger_config' )
        self.parser.add_argument('--dataset_name', type = str, default = None, help = 'which model do you choose')
        self.parser.add_argument('--model_name', type = str, default = None, help = 'which model do you choose')
        self.parser.add_argument('--model_config', type = str, default = None, help = 'where is the model_config')