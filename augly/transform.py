import logging

import cv2

from augly.img import save, load


class LoadDir:
    def __init__(self, dirpath):
        logging.info(dirpath)


def scale(data):
    logging.info(data.labels)

def gray_scale(filepath):
    img_arr = load(filepath)
    gray_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
    save(gray_arr, "gray", filepath)
