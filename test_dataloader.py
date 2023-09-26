import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
from logger import My_logger
training_data = datasets.MNIST(
    root = "dataset",
    train = True,
    download = True,
    transform = ToTensor(),
)

test_data = datasets.MNIST(
    root = 'dataset',
    train = False,
    download = True,
    transform = ToTensor(),
)
batch_size = 64
log = My_logger().logger
train_dataloader = DataLoader(training_data, batch_size = batch_size)
test_dataloader = DataLoader(test_data, batch_size = batch_size)
for X,y in train_dataloader:
    log.info(f"shape of X [N,C,H,W]:{X.shape}")
    log.info(f"shape of y:{y.shape}{y.dtype}")
    break