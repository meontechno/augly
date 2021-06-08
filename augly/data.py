import os
import logging


class Load:
    def __init__(self, path, isdir=True, load_labels=False):
        self.path = path
        self.isdir = isdir
        self.load_labels = load_labels
        self.images, self.labels = self.list()

    def list(self):
        images = []
        labels = []
        if self.isdir:
            for file in os.listdir(self.path):
                if file.endswith((".jpg", ".png")):
                    images.append(os.path.join(self.path, file))
                if file.endswith((".txt", ".xml")):
                    labels.append(os.path.join(self.path, file))
        return images, labels

