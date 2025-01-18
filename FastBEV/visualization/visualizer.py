import cv2
import numpy as np
import matplotlib.pyplot as plt

def visualize_lidar_to_image(lidar_points, camera_info, output_path):
    corners_img, valid = lidar_to_img(lidar_points, camera_info)
    valid_corners = corners_img[valid]
    image = cv2.imread(camera_info['image_path'])
    for corner in valid_corners:
        cv2.circle(image, tuple(corner), radius=5, color=(0, 0, 255), thickness=2)
    cv2.imwrite(output_path, image)

def lidar_to_img(lidar_points, camera_info):

    lidar2camera = np.array(camera_info['lidar2img']['extrinsic'], dtype=np.float32)
    camera2img = np.array(camera_info['lidar2img']['intrinsic'], dtype=np.float32)

    lidar_points_homogeneous = np.hstack([lidar_points, np.ones((lidar_points.shape[0], 1))])
    camera_points_homogeneous = lidar_points_homogeneous @ lidar2camera.T
    valid = camera_points_homogeneous[:, 2] > 0  # Only keep points in front of the camera

    camera_points = camera_points_homogeneous[valid, :3]
    camera_points /= camera_points[:, 2:3]  # Normalize to image plane
    img_points = camera_points @ camera2img.T

    return img_points[:, :2], valid
