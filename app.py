import os
import logging

import cv2

from augly import transform
from augly import data


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = data.Load('./test')
    transform.scale(data)
    #for file in os.listdir("./test"):
     #   if file.endswith('.jpg'):
      #      transform.gray_scale(os.path.join("./test", file))
            #gray_scale("./test/test.jpg")

