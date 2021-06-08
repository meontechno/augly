import os
import logging

import cv2

from augly import transform
from augly import data


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = data.Load('./test', load_labels=True)
    transform.scale(data)
