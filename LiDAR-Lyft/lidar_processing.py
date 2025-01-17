from lyft_dataset_sdk.utils.data_classes import LidarPointCloud
from lyft_dataset_sdk.lyftdataset import LyftDataset
from lyft_dataset_sdk.utils.geometry_utils import view_points
import numpy as np

def process_lidar_points(lyft_data: LyftDataset, lidar_token: str):
    """Processes LiDAR point cloud data."""
    sd_record = lyft_data.get("sample_data", lidar_token)
    lidar_file = sd_record['filename']

    # Load point cloud
    lidar_points = LidarPointCloud.from_file(lidar_file)

    # Transform to ego vehicle frame
    cs_record = lyft_data.get("calibrated_sensor", sd_record['calibrated_sensor_token'])
    vehicle_from_sensor = np.eye(4)
    vehicle_from_sensor[:3, :3] = cs_record['rotation']
    vehicle_from_sensor[:3, 3] = cs_record['translation']

    points = view_points(
        lidar_points.points[:3, :], vehicle_from_sensor, normalize=False
    )

    return points