from models.trt_model_pre import TRTModelPre
from models.trt_model_post import TRTModelPost
from preprocessing.image_processing import preprocess_images
from postprocessing.decoding import decode
from visualization.visualizer import visualize_bev
from utils.file_utils import ensure_dir, save_tensor
import os
import torch

def main():
    output_dir = './output'
    ensure_dir(output_dir)

    model_path = './model/fastbev.pth'
    trt_model_pre = TRTModelPre.load(model_path, device='cuda')
    trt_model_post = TRTModelPost.load(model_path, device='cuda')

    image_paths = ['path_to_image1.jpg', 'path_to_image2.jpg']
    batch_images = preprocess_images(image_paths)

    with torch.no_grad():
        pre_output = trt_model_pre(batch_images)

    decoded_boxes = decode(pre_output)

    visualize_bev(decoded_boxes, scores=[0.9, 0.8])  # Example scores

    save_tensor(pre_output, os.path.join(output_dir, 'pre_output.pth'))

if __name__ == "__main__":
    main()
