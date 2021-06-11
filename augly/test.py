import os

import cv2


def get_labels(label_path):
    labels = []
    for line in fileinput.input(label_path, inplace=1):
        split_label = line.split(' ')
        labels.append([split_label[1], split_label[2], split_label[3], split_label[4]])
    return labels


def convert_yolo_to_default(cordinates, height, width):
    #c_x = int(cordinates[0] * width)
    #c_y = int(cordinates[1] * height)
    #w = int(cordinates[2] * weight)
    #h = int(cordinates[3] * height)
    x = int(cordinates[0] * width) - int(cordinates[2] * weight) / 2
    y = int(cordinates[1] * height) - int(cordinates[3] * height) / 2



def draw_bounding_box(image_path, label_path):
    labels = get_cordinates(label_path)
    img_arr = cv2.imread(image_path)
    color = (255, 0, 0)

    cv2.rectangle(image_arr, (label[0], label[1]), (label[0]+width, label[0]+height), color, 2)
    cv2.imshow("Frame", image_arr)

