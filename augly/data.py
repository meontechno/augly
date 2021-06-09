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
    """Loads image data at a directory level or a single file.
    
    Label files (txt, xml etc) corresponding to the images can be loaded
    to apply image transformations.
    
    Args:
        path: `PathLike` object that represents a dir/file path
        load_labels: Boolean. True to load corresponding label file for
            transformation
        label_type: label file type to load. txt/xml
    
    """
    def __init__(self, path, load_labels=False, label_type="txt"):
        self.path = path
        self.load_labels = load_labels
        self.label_type = label_type
        self.images, self.labels, self.missing_labels = self.list()

    
    def list(self):
        (images, labels, missing_labels) = ([], [], [])
        supported_types = (".jpg", ".jpeg", ".png")
        if self.path.endswith(supported_types):
            images.append(self.path)
            if not self.verify_label():
                missing_labels.append(self.path)
        else:
            for file in os.listdir(self.path):
                if file.endswith(supported_types):
                    images.append(os.path.join(self.path, file))
                    if self.load_labels:
                        if not self.verify_labels(file):
                            missing_labels.append(file)
        return images, labels, missing_labels


    def verify_label(self):
        split = self.path.rsplit('/')
        label = split[1].rsplit('.')[0] + '.' + self.label_type
        return os.path.isfile(os.path.join(split[0], label))

    def verify_labels(self, file):
        label = file.rsplit('.')[0] + "." + self.label_type
        return os.path.isfile(os.path.join(self.path, label))
