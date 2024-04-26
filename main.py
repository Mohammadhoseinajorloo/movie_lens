from constants import *
from tabulate import tabulate
import pandas as pd 
import os

class Dataset:

    def __init__(self, path):
        self.path = path
        if self.__is_multi_file(self.path):
            self.__merge_files(self.path)
        else:
            __file = str(os.listdir(self.path)[0])
            __file_path = os.path.join(self.path, __file)
            self.dataset = pd.read_csv(__file_path)

    def __merge_files(self, directory):
        pass

    def __is_multi_file(self, directory):
        count_file = len(os.listdir(directory))
        if count_file == 0:
            raise Exception("Empty file")
        elif count_file != 1:
            return True
        return False

    def __repr__(self):
        metadata = self.dataset.values
        head = self.dataset.columns
        return tabulate (metadata, headers=head, tablefmt="grid")[:1000]

if __name__ == '__main__':
    dataset = Dataset(PATH)
    print(dataset)
