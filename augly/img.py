import os
import logging
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


def save(img, op, filepath, overwrite=True):
    """

    """
    timestamp = datetime.datetime.now().strftime("%m%d%H%M%S%f%Z")
    filepath = path_to_string(filepath)
    name = filepath.rsplit('.', 1)[0]
    ext = filepath.rsplit('.', 1)[1]
    logging.info(name+op+timestamp+'.'+ext)
    cv2.imwrite(name+op+timestamp+'.'+ext, img)


def load(filepath):
    """

    """
    filepath = path_to_string(filepath)
    return cv2.imread(filepath)
