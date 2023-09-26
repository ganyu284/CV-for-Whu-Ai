import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from register import Registers
class dataloader:
    pass

@Registers.dataloader.register
class Minstdataloader(dataloader):
    def output():
        print("this is Minstdataloader")

