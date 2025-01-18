import numpy as np

def lidar_to_points(lidar_file):

    lidar_points = np.fromfile(lidar_file, dtype=np.float32).reshape(-1, 4)  # Assuming 4 channels (x, y, z, intensity)
    return lidar_points[:, :3]  # Return only (x, y, z)

def transform_lidar_to_vehicle_frame(lidar_points, calibration_matrix):
    lidar_points_homogeneous = np.hstack([lidar_points, np.ones((lidar_points.shape[0], 1))])
    transformed_points = lidar_points_homogeneous @ calibration_matrix.T
    return transformed_points[:, :3]

def view_points(points, transformation_matrix):
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = points_homogeneous @ transformation_matrix.T
    return transformed_points[:, :3]
