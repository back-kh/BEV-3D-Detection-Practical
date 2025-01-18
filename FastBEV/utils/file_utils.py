import os
import torch

def save_tensor(tensor, file_path):
    torch.save(tensor, file_path)

def load_tensor(file_path):
    return torch.load(file_path)
