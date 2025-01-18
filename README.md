# BEV-Practical
BEV-3D detection implementation represents the state-of-the-art in practical applications, offering cutting-edge solutions for real-world challenges in autonomous driving, robotics, and advanced perception systems.

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
1. **Prepare the Dataset**
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
# 2. Fast BEV: LiDAR Data Processing and Visualization

**Fast BEV** is a high-performance deep learning model for Bird's Eye View (BEV) detection from LiDAR data. It processes LiDAR point clouds for object detection and visualizes the results in BEV and camera image views. The system supports both PyTorch and ONNX models for efficient inference.
***Prepare the Dataset***
Download the LiDAR dataset and store it in a folder (e.g., data/).
Update the image_paths in main.py to point to the image files.
### Requirements

- torch==2.0.0
- torchvision==0.15.0
- torchaudio==2.0.0
- moviepy
- numpy
- onnx==1.14.0
- onnxruntime==1.14.0
- opencv-python==4.6.0
- scipy==1.9.0
- matplotlib==3.5.1
- pillow==9.2.0
- moviepy==1.0.3
- pyquaternion==0.9.5
- onnxruntime-gpu==1.14.0
- tqdm==4.64.0
- scikit-learn==1.1.1
- mmcv==2.0.0
- mmdet==3.0.0

