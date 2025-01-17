## 1) LiDAR Data Processing and Visualization for Lyft Dataset
This project processes and visualizes LiDAR data from the Lyft dataset. It includes modular components for loading the dataset, processing LiDAR points, and creating visualizations such as plots and videos.

### Folder Structure

```
project_root/
├── main.py                # Entry point for running the project
├── data_loader.py         # Loads the Lyft dataset
├── visualization.py       # Handles plotting and video creation
├── lidar_processing.py    # Processes raw LiDAR data
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
```
### Requirements

- Python 3.7+
- Lyft Dataset SDK
- matplotlib
- moviepy
- numpy
- 1. **Prepare the Dataset**
   - Download the Lyft dataset and place it in a folder (e.g., `data/`).

2. **Run the Main Script**
   ```bash
   python main.py --data_path <path_to_data> --json_path <path_to_json> --output_path <output_folder>
   ```
   - `<path_to_data>`: Path to the dataset folder (e.g., `./data`).
   - `<path_to_json>`: Path to the dataset JSON files.
   - `<output_folder>`: Path where visualizations and outputs will be saved.

### Features

1. **LiDAR Frame Plotting**:
   - Generates a scatter plot of LiDAR points for a single frame.

2. **Scene Video Creation**:
   - Creates a video visualizing LiDAR data for an entire scene.

### Example Command

```bash
python main.py --data_path ./data --json_path ./data/json --output_path ./output
```

### Modular Components

#### `data_loader.py`
- Loads the Lyft dataset using the Lyft Dataset SDK.

#### `visualization.py`
- Functions for:
  - Plotting individual LiDAR frames.
  - Creating videos of entire scenes.

#### `lidar_processing.py`
- Processes LiDAR point cloud data and transforms it into the ego vehicle frame.

#### `utils.py`
- Contains utility functions such as ensuring directories exist.
