# data_loader.py

from lyft_dataset_sdk.lyftdataset import LyftDataset

def load_lyft_data(data_path, json_path):
    """Loads the Lyft dataset."""
    print("Loading Lyft dataset...")
    return LyftDataset(data_path=data_path, json_path=json_path, verbose=True)
