from PIL import Image
import numpy as np
import torch
from config import DEVICE, MEAN, STD, INPUT_SIZE

def preprocess_images(image_paths):
    images = []
    for path in image_paths:
        img = Image.open(path).convert('RGB')
        img_resized = img.resize(INPUT_SIZE[::-1], Image.LANCZOS)
        img_tensor = torch.from_numpy(np.array(img_resized)).float().to(DEVICE).permute(2, 0, 1)
        img_normalized = (img_tensor - MEAN.view(-1, 1, 1)) / STD.view(-1, 1, 1)
        images.append(img_normalized)
    return torch.stack(images, dim=0)
