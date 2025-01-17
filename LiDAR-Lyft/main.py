from data_loader import load_lyft_data
from visualization import plot_lidar_frame, create_scene_video
import argparse

def main():
    parser = argparse.ArgumentParser(description="LiDAR Data Processing and Visualization for Lyft Dataset")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the dataset folder")
    parser.add_argument("--json_path", type=str, required=True, help="Path to the dataset JSON files")
    parser.add_argument("--output_path", type=str, required=True, help="Path to save visualizations and outputs")
    args = parser.parse_args()

    # Load Lyft dataset
    lyft_data = load_lyft_data(args.data_path, args.json_path)

    # Visualize a single LiDAR frame
    sample_token = lyft_data.scene[0]["first_sample_token"]
    plot_lidar_frame(lyft_data, sample_token, args.output_path)

    # Create a scene video
    scene_token = lyft_data.scene[0]["token"]
    create_scene_video(lyft_data, scene_token, args.output_path)

if __name__ == "__main__":
    main()
