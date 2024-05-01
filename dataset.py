import pandas as pd
import os

class Dataset:

    def __init__(self, path):
        self.path = path
        self.dataframes = {}
        self._read_data(self.path)

    # detect format file and read with methode in pandas library
    def _read_data(self, directory: str):
        '''
        This function two worke doing:
        1. detect format file
        2. read file with spesial methode in pandas library
        input : str -> path directory
        output : update self.dataframes
        '''
        files = os.listdir(directory)
        for file in files:
            if file.endswith('.csv'):
                self.dataframes[file.split('.')[0]] = pd.read_csv(os.path.join(directory, file))
            # TODO:added other format e.x:
            elif file.endswith('.xlsx'):
                pass

    def __repr__(self) -> str:
        text:str = ''
        dic = {}
        index = ['row', 'column']
        for k, v in self.dataframes.items():
            dic[k] = v.shape
        text += f'{pd.DataFrame(dic, index=index)}'
        return text
