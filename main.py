from constants import *
from functools import reduce
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

    # merge all file in data folder in one dataframe and delet columns some.
    def __merge_files(self, directory: str) -> dataframe:
        '''
        input : path string
        output : dataframe 
        directory : directory path
        '''
        dataframes = []
        file_paths = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
        sorted_files = sorted(file_paths, key=os.path.getsize, reverse=True)
        for file in sorted_files:
            df = pd.read_csv(file)
            dataframes.append(df)
        self.dataset = reduce(lambda left,right: pd.merge(left,right,on=['movieId'], how='outer'), dataframes)
        self.dataset = self.dataset.drop(columns=['userId_x', 'timestamp_x'])
        self.dataset.columns = ['movieId', 'rating', 'title', 'genres', 'imdbId', 'tmdbId', 'userId','tag', 'timestamp']
        print(self.dataset)
        return self.dataset


    def __is_multi_file(self, directory):
        count_file = len(os.listdir(directory))
        if count_file == 0:
            raise Exception("Empty file")
        elif count_file != 1:
            return True
        return False

#    def __repr__(self):
#        metadata = self.dataset.values
#        head = self.dataset.columns
#        return tabulate (metadata, headers=head, tablefmt="grid")

if __name__ == '__main__':
    dataset = Dataset(PATH)
