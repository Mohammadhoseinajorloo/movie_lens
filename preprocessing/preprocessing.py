import pandas as pd
import numpy as np
from tqdm import tqdm
import time

class Preprocessing:

    def __init__(self, df):
        self.df = df

    def drop_duplicates(self, columns=None):
        if columns == None:
            self.df.drop_duplicates(inplace=True)
        else:
            self.df.drop_duplicates(subset=columns, inplace=True)

    def check_missing_data(self, verbos=False):
        proportion_null_rows = 100*(round(self.df.isnull().sum()/self.df.count(), 2))
        if proportion_null_rows.all() <= 5:
            if verbos:
                print(f"There are {self.df.isnull().sum().sum()} rows with a null value. All of them are erased!")
            self.df.dropna()
        else:
            if verbos == True:
                print("Too many null values, we need to check columns by columns further.")
            if df.isnull().sum().sum() > 0:
                if verbos:
                    print("\nProportion of missing values by column")
                value = 100*(round(self.df.isnull().sum()/df.count(), 2))
                print(value)
                self._dealing_missing_data(df)
            else:
                print('No missing values detected')


    def find_outliers_IQR(self, coefficient):
        outlier_indices = []
        df = self.df.select_dtypes(include=['number'])
        for column in df.columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - coefficient * IQR 
            upper_bound = Q3 - coefficient * IQR
            outlier_list_col = df [(df[column] < lower_bound) | df[column] > upper_bound].index
            outlier_indices.extend(outlier_list_col)
        outlier_indices = list(set(outlier_indices))
        df.iloc[outlier_indices]
        return outlier_indices


    def content_table(self, series: pd.Series) -> pd.DataFrame:
        '''
        This function vlaue into a series convert to column
        header and index per fill in eche columns.
        input:
            series -> content series whith need convert to header columns
        output:
            dataframe -> finaly dataframe with seting values
        '''
        pbar1 = tqdm(desc='processing index', leave=False, total=len(series))
        pbar2 = tqdm(desc='processing item', leave=False, total=len(series))
        pbar3 = tqdm(desc='processing columns', leave=False, total=len(series))
        content_set = self._content_set(series)
        row = series.shape[0]
        column = len(content_set)
        shape = (row, column)
        zero_array = np.zeros(shape)
        df_zeros = pd.DataFrame(zero_array, columns=content_set)
        for i, value in enumerate(series):
            value = value.split("|")
            pbar1.update(1)
            for item in value:
                pbar2.update(1)
                for c in df_zeros.columns:
                    if item == c:
                        df_zeros.loc[i,c] = 1
                    pbar3.update(1)
        return df_zeros


    def split_title_year(self, x: str) -> str | int :
        '''
        in function yek string ke shamel titile har film va sal sakhte an mishavad ra migirad va title va sal sakht ra az ham joda mkondad va be onvan 2 moalefe bazmigardanad\
        input:
            x -> str - name va sal sakhte be surat yek srting yek parche 
        output:
            title -> str - name yek film
            year -> int - sla sakhte an film

        '''
        title = " ".join(x.split(" ")[:-1])
        year = x.split(" ")[-1][1:-1]
        return title, year


    def _content_set(self, series:pd.Series) -> list:
        '''
        This function in input series and a list at unique values.
        input:
            series -> ghesmati as yek dataframe ke value haye dakhe
        l an daraye charcter manand "-/|_!@#$%^&*+" bashe
        output: 
            list -> listi az meghdar haye uniqeue
        '''
        content = []
        for row in series.values:
                row = row.split("|")
                for item in row:
                    if item in content:
                        continue
                    content.append(item)
        return content


    def _dealing_missing_data(self):
        value = 100*(round(self.df.isnull().sum()/df.count(), 2))
        to_delete = []
        to_impute = []
        to_check = []
        for name , proportion in value.items():
            if int(proportion) == 0:
                continue
            elif int(proprtion) <= 10:
                to_impute.append(name)
                df.fillna(df[name].median())
            else:
                to_check.append(name)
        print(f"\nThe missing values in {to_impute} have been replaced by the median.")
        print(f"The columns {to_check} should be further understood")
