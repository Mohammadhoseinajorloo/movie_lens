from .path import Path
import pandas as pd
import os

class Reader:
    def __init__(self, filename):
        self.path_obj = Path(filename)
        self.path = self.path_obj.address

    def _whatformat(self):
         return self.path_obj.file_object.extention

    def reader(self):
        format = self._whatformat()
        if format == "csv":
            return pd.read_csv(self.path)
        if format == "json":
            return pd.read_json(self.path)
        if format in ['xls', 'xlsx']:
            return pd.read_excel(self.path)
        raise ValueError('Unknown file format!!!')

    def __repr__(self):
        _str = ""
        _str += f"{self.path}"
        return _str
