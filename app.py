import logging

import cv2

from augly.transform import gray_scale
from augly.img import load, save


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    img_arr = load('./test/test.jpg')
    save('/test/gray.jpg')
    cv2.imshow("gray", gray_scale(img_arr))
    cv2.waitKey(0)
