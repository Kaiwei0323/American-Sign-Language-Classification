from IPython.display import Image, display
import torch
import glob

# Fix a seed for PyTorch
torch.manual_seed(4200);

## ===========================
##   GPU
## ===========================

gpu = True

if gpu == True:
    device = torch.device('cuda')
else:
    device = torch.device('cpu')