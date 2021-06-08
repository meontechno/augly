# MIT License

# Copyright (c) 2021 meontechno

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Contains the data loader class and other data related API entries."""

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
