import os
import logging

import cv2

from augly import transform
from augly import data


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    dataset = data.Load('./test', load_labels=True)
    #transform.scale(data)
    logging.info(dataset.stats())
