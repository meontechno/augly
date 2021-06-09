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
        if not os.path.exists(path):
            raise ValueError("Invalid file/directory path")
        
        self.path = path
        self.load_labels = load_labels
        self.label_type = label_type
        self.data_dict = self.generate_data_dict()

    
    def generate_data_dict(self):
        data_dict = {}
        supported_types = (".jpg", ".jpeg", ".png")
        if os.path.isfile(self.path):
            if not self.path.endswith(supported_types):
                raise ValueError("Image format not supported. (jpg, jpeg, png)")
            data_dict[self.path] = self.get_label(self.path) if self.load_labels else None
        else:
            for file in os.listdir(self.path):
                if file.endswith(supported_types):
                    file_path = os.path.join(self.path, file)
                    data_dict[file_path] = self.get_label(file_path) if self.load_labels else None
        return data_dict


    def get_label(self, file_path):
        split = file_path.rsplit('/', 1)
        label = split[1].rsplit('.', 1)[0] + '.' + self.label_type
        label_path = os.path.join(split[0]+'/', label)
        if not os.path.isfile(label_path):
            return None
        return label_path

    def stats(self):
        images = len(self.data_dict)
        labels = sum(value is not None for value in self.data_dict.values()) 
        missing = sum(value is None for value in self.data_dict.values())
        return (("Total images", images), ("Total labels", labels), ("Total missing", missing))


