import pandas as pd

class Preprocessing:

    def __init__(self, dataframes):
        self.dataframes = dataframes

    def merging(self):
        return pd.concat(self.dataframes, axis=1)

    def bineryzation(self, colume):
        unique_value = self._unique_value(colume)
        print(unique_value)

    def _unique_value(colume):
        for row in colume:
            print(row)

