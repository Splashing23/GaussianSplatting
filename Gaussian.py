import torch
from torch import nn
from torch import exp, transpose, inverse



class Gaussian(nn.Module):
    def __init__(self):
        self.mean = torch.tensor([])
        self.covar = torch.tensor([])
        self.sh = 

    def get_sample(self, x):
        return exp(-0.5 * transpose(x) * inverse(self.covar()) )