from .__init__ import PARENT
from .file import File
import os

class Path:

    parent = PARENT

    def __init__(self, file):
        self.file_object = File(file)
        self.filename = self.file_object.name
        self.format = self.file_object.extention
        self.address = os.path.join(self.parent, self.filename+"."+self.format)

    def __repr__(self):
        _str = ''
        _str = f"parent: {self.parent}\nfilename: {self.filename}\nformat: {self.format}"
        return _str
