import os

def ensure_dir(directory):
    """Ensures a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")