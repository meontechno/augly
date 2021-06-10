import os
import datetime

import cv2


def path_to_string(path):
    """Convert `PathLike` objects to their string representation.
    
    If given a non-string typed path object, converts it to its string
    representation.
    
    If the object passed to `path` is not among the above, then it is
    returned unchanged. This allows e.g. passthrough of file objects
    through this function.
    
    Args:
        path: `PathLike` object that represents a path
    Returns:
        A string representation of the path argument, if Python support exists.
    """
    if isinstance(path, os.PathLike):
        return os.fspath(path)
    return path


def save_img(img_arr, operation, save_path):
    """Save image with timestamp and operation name attached.

    Args:
        img_arr: opencv image array
        operation: name of the transformation operation
        save_path: full save path for the image
    """
    timestamp = datetime.datetime.now().strftime("%m%d%H%M%S%f%Z")
    save_path = path_to_string(save_path)
    name = save_path.rsplit('.', 1)[0]
    ext = save_path.rsplit('.', 1)[1]
    cv2.imwrite(name+operation+timestamp+'.'+ext, img_arr)
