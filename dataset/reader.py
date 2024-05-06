from .path import Path
import pandas as pd
import os

class Reader:
    def __init__(self, filename):
        self.path_object = Path(filename)
        self.path = self.path_object.address

    def _whatformat(self):
         return self.path_object.file_object.extention

    def reader(self):
        format = self._whatformat()
        if format == "csv":
            dataframe = pd.read_csv(self.path)
        # TODO: add other format for reader data
        return dataframe

    def __repr__(self):
        _str = ""
        _str += f"{self.path}"
        return _str
