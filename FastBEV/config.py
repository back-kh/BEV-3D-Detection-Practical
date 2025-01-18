import os
import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
MODEL_ROOT_PATH = 'model/tidl'
INPUT_SIZE = (256, 704)  # (height, width)
MEAN = torch.tensor([123.675, 116.28, 103.53], dtype=torch.float32).to(DEVICE)
STD = torch.tensor([58.395, 57.12, 57.375], dtype=torch.float32).to(DEVICE)
