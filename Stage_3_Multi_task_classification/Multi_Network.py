import torch.nn as nn
import torch.nn.functional as F

class multiNet(nn.Module):
    def __init__(self):
        super (multiNet, self).__init__()
        self.conv1=nn.Conv2d(3,3,3)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool1 = nn.MaxPool2d(kernel_size=2)

        self.conv2=nn.Conv2d(3,6,3)
        self.relu2=nn.ReLU(inplace=True)
        self.pool2=nn.MaxPool2d(kernel_size=2)

        self.fc1=nn.Linear(6*123*123,150)
        self.relu3=nn.ReLU(inplace=True)

        self.dropout=nn.Dropout2d()

        self.fc2=nn.Linear(150,2)
        self.softmax1 = nn.Softmax(dim=1)

        self.fc3=nn.Linear(150,3)
        self.softmax2=nn.Softmax(dim=1)

    def forward(self,x):
        x=self.conv1(x)
        x=self.relu1(x)
        x=self.pool1(x)

        x=self.conv2(x)
        x=self.relu2(x)
        x=self.pool2(x)

        x = x.view(-1, 6 * 123 * 123)
        x=self.fc1(x)
        x=self.relu3(x)

        x = F.dropout(x, training=self.training)

        x_classes = self.fc2(x)
        x_classes = self.softmax1(x_classes)

        x_species=self.fc3(x)
        x_species=self.softmax2(x_species)
        return x_classes,x_species