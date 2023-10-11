import torch
import torch.nn as nn
import torch.nn.functional as F
from register import Registers
class BaseModel:
    pass

@Registers.model.register
class letnet5(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.conv1 = nn.Conv2d(1,6,5)
        self.pool2 = nn.MaxPool2d(2,2)
        self.conv3 = nn.Conv2d(6,16,5)
        self.pool4 = nn.MaxPool2d(2,2)
        self.fc5 = nn.Linear(16*4*4,120)
        self.fc6 = nn.Linear(120,64)
        self.fc7 = nn.Linear(64,10)
    def foward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool2(x)
        x = F.relu(self.conv3(x))
        x = self.pool4(x)
        x = x.view(-1, 16*4*4)
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))
        x = self.fc7(x)
        return x
    def output():
        print("Here is letnet5") 