import logging

import cv2


def gray_scale(img_arr):
    gray_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
    return gray_arr
