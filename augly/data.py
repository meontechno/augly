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


class Load:
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
    def __init__(self, path, isdir=True, load_labels=False, label_type="txt"):
        self.path = path
        self.isdir = isdir
        self.load_labels = load_labels
        self.label_type = label_type
        self.images, self.labels, self.missing_labels = self.list()

    
    def list(self):
        (images, labels, missing_labels) = ([], [], [])
        if self.isdir:
            for file in os.listdir(self.path):
                if file.endswith((".jpg", ".jpeg", ".png")):
                    images.append(os.path.join(self.path, file))
                    if self.load_labels:
                        if not self.verify_label(file):
                            missing_labels.append(file)
        return images, labels, missing_labels

    
    def verify_label(self, file):
        label = file.rsplit('.')[0] + "." + self.label_type
        return os.path.isfile(os.path.join(self.path, label))

