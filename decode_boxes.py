import numpy as np

def filter_box(output, img_width, img_height):

    boxes = []
    scores = []
    grid_size = 16

    for i in range(grid_size):
        for j in range(grid_size):

            box = output[i, j, 0, 1:]
            score = output[i, j, 0, 0]

            if score > 0.5:
                x = ((box[0] + j)/grid_size) * img_width
                y = ((box[1] + i)/grid_size) * img_height
                w = box[2] * img_width
                h = box[3] * img_height

                boxes.append([x - w/2, y - h/2, x + w/2, y + h/2])
                scores.append(score)

    return boxes, scores



def iou(box1, box2):

    xi1 = max(box1[0], box2[0])
    yi1 = max(box1[1], box2[1])
    xi2 = min(box1[2], box2[2])
    yi2 = min(box1[3], box2[3])

    inter_area = (xi2 - xi1) * (yi2 - yi1)

    box1_area = (box1[3] - box1[1])*(box1[2]- box1[0])
    box2_area = (box2[3] - box2[1])*(box2[2]- box2[0])

    union_area = (box1_area + box2_area) - inter_area

    iou = inter_area / union_area

    return iou



def non_max_supression(boxes, scores, iou_value):

    scores = np.array(scores)
    sort_scores = scores.argsort().tolist()

    no_supress = []

    while(len(sort_scores)):

        index = sort_scores.pop()
        no_supress.append(index)

        if len(sort_scores) == 0:
            break

        iou_list = []
        for i in sort_scores:
            iou_list.append(iou(boxes[i], boxes[index]))
        
        iou_list = np.array(iou_list)
        index = (iou_list > iou_value).astype(int)

        sort_scores = [sort_scores[i] for i in range(len(index)) if index[i] == 0]

    final_boxes = []
    for i in no_supress:
        final_boxes.append(boxes[i])

    return final_boxes


def get_boxes(output, iou_value, img_width, img_height):

    boxes, scores = filter_box(output, img_width, img_height)

    boxes = non_max_supression(boxes, scores,iou_value)

    return boxes
