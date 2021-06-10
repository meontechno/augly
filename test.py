import os
import logging

import cv2

from augly.transform import transform as tr
from augly import data


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    dataset = data.Load('./test', load_labels=True)
    logging.info(dataset.stats())
    dataset.apply([tr.gray_scale])
