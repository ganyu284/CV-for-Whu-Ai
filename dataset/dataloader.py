import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from register import Registers
from logger import My_logger
import sys
import os
import yaml

class dataloader:
    pass

@Registers.dataloader.register
class Minstdataloader(dataloader):
    def output():
        print("this is Minstdataloader")
    def __init__(self, dataloader_args_path = None) -> None:
        super().__init__()
        if dataloader_args_path is None:
            dataloader_args_path ='config/dataloader/MNIST_dataloader.yaml'
        if os.path.exists(dataloader_args_path):
            with open(dataloader_args_path, 'r' , encoding = 'utf_8') as f:
                config = yaml.load(stream = f, Loader = yaml.FullLoader)
        self.train_data = datasets.MNIST(
            root = config['root'],
            train = config['trainloader_train'],
            download = config['trainloader_download'],
            transform = transforms.ToTensor(),
        )
        self.test_data = datasets.MNIST(
            root = config['root'],
            train = config['testloader_train'],
            download = config['testloader_download'],
            transform =transforms.ToTensor,
        )
        self.log = My_logger().logger
        self.train_dataloader = DataLoader(self.train_data, batch_size = config['batch_size'])
        self.test_dataloader = DataLoader(self.test_data, batch_size = config['batch_size'])
    def output_size(self):
        for X,y in self.train_dataloader:
            self.log.info(f"shape of X [N,C,H,W]:{X.shape}")
            self.log.info(f"shape of y:{y.shape}{y.dtype}")
            break