from contstant import PARENT
from file import File
import os

class Path:

    parent = PARENT

    def __init__(self, file):
        self.file = File(file) 
        self.path = os.path.join(self.parent, self.file)

    def __repr__(self):
        _str = ''
        _str = f"{self.path}"
        return _str
