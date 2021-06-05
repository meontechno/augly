import logging

import cv2

from augly.img import save, load


def gray_scale(filepath):
    img_arr = load(filepath)
    gray_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
    save(gray_arr, "gray", filepath)
