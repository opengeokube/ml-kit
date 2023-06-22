from torch.utils.data import random_split
from torchvision import transforms
from torchvision.datasets import MNIST

from mlkit import MLKitAbstractDataModule


class MNISTCustomDataset(MLKitAbstractDataModule):
    def prepare_trainvaldataset(self, root_dir: str):
        dset = MNIST(
            root=root_dir,
            train=True,
            download=True,
            transform=transforms.ToTensor(),
        )
        train_dset, val_dset = random_split(dset, [0.8, 0.2])
        return (train_dset, val_dset)

    def prepare_testdataset(self, root_dir: str):
        return MNIST(
            root=root_dir,
            train=False,
            download=True,
            transform=transforms.ToTensor(),
        )
