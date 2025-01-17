import matplotlib.pyplot as plt
from moviepy.editor import ImageSequenceClip
from lidar_processing import process_lidar_points
import os

def plot_lidar_frame(lyft_data, sample_token, output_path):
    """Plots a single LiDAR frame."""
    sample = lyft_data.get('sample', sample_token)
    lidar_token = sample['data']['LIDAR_TOP']
    lidar_points = process_lidar_points(lyft_data, lidar_token)

    plt.figure(figsize=(10, 10))
    plt.scatter(lidar_points[0, :], lidar_points[1, :], s=0.1, c=lidar_points[2, :])
    plt.title("LiDAR Point Cloud")
    plt.xlabel("X")
    plt.ylabel("Y")

    output_file = os.path.join(output_path, f"lidar_frame_{sample_token}.png")
    plt.savefig(output_file)
    plt.close()
    print(f"Saved LiDAR frame to {output_file}")

def create_scene_video(lyft_data, scene_token, output_path):
    """Creates a video for a scene using LiDAR data."""
    scene = lyft_data.get('scene', scene_token)
    first_sample_token = scene['first_sample_token']

    frames = []
    sample_token = first_sample_token

    while sample_token:
        sample = lyft_data.get('sample', sample_token)
        lidar_token = sample['data']['LIDAR_TOP']
        lidar_points = process_lidar_points(lyft_data, lidar_token)

        # Generate frame plot
        plt.figure(figsize=(10, 10))
        plt.scatter(lidar_points[0, :], lidar_points[1, :], s=0.1, c=lidar_points[2, :])
        plt.title("LiDAR Point Cloud")
        plt.xlabel("X")
        plt.ylabel("Y")

        frame_path = os.path.join(output_path, f"frame_{sample_token}.png")
        plt.savefig(frame_path)
        plt.close()
        frames.append(frame_path)

        # Get next sample
        sample_token = sample['next']

    # Create video
    clip = ImageSequenceClip(frames, fps=5)
    video_path = os.path.join(output_path, "scene_video.mp4")
    clip.write_videofile(video_path, codec="libx264")
    print(f"Saved scene video to {video_path}")

    # Cleanup temporary frames
    for frame in frames:
        os.remove(frame)