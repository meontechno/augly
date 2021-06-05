import os
import logging

import cv2

from augly.transform import gray_scale


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    for file in os.listdir("./test"):
        if file.endswith('.jpg'):
            gray_scale(os.path.join("./test", file))
            #gray_scale("./test/test.jpg")

