import numpy as np

def box_overlap(box_a, box_b):

    # Intersection over union (IoU) for rotated bounding boxes
    # Box format: [x_center, y_center, width, height, angle]
    box_a_corners = get_box_corners(box_a)
    box_b_corners = get_box_corners(box_b)
    
    # Find intersection points and compute area
    intersection_points = find_intersection_points(box_a_corners, box_b_corners)
    return calculate_area_of_polygon(intersection_points)

def nms_cpu(boxes, scores, nms_thresh):

    order = scores.argsort()[::-1]
    keep = []
    suppressed = np.zeros(len(scores), dtype=bool)

    for idx in order:
        if suppressed[idx]:
            continue
        keep.append(idx)
        center = boxes[idx, :2]
        distances = np.linalg.norm(boxes[:, :2] - center, axis=1)
        suppressed = suppressed | (distances < nms_thresh)

    return keep

def find_intersection_points(box_a_corners, box_b_corners):

    pass

def calculate_area_of_polygon(corners):

    pass
