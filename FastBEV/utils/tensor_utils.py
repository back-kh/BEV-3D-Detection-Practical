import torch

def tensor_to_numpy(tensor):
    """Convert a tensor to a numpy array."""
    return tensor.cpu().numpy()

def numpy_to_tensor(np_array):
    """Convert a numpy array to a tensor."""
    return torch.from_numpy(np_array).float()
