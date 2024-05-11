import pandas as pd

class Preprocessing:

    def __init__(self, dfs):
        self.dfs = dfs

    def drop_duplicates(self, columns=None):
        for df in self.dfs:
            if columns == None:
                df.drop_duplicates(inplace=True)
            else:
                df.drop_duplicates(subset=columns, inplace=True)

    def check_missing_data(self):
        for df in self.dfs:
            proportion_null_rows = 100*(round(df.isnull().sum()/df.count(), 2))
            if proportion_null_rows.all() <= 5:
                print(f"There are {df.isnull().sum()} rows with a null value. All of them are erased!")
                df.dropna()
            else:
                print("Too many null values, we need to check columns by columns further.")
                if df.isnull().sum().sum() > 0:
                    print("\nProportion of missing values by column")
                    value = 100*(round(df.isnull().sum()/df.count(), 2))
                    print(value)
                    self._dealing_missing_data(df)
                else:
                    print('No missing values detected')

    def _dealing_missing_data(self):
        for df in self.dfs:
            value = 100*(round(df.isnull().sum()/df.count(), 2))
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

    def find_outliers_IQR(self, coefficient):
        outlier_indices = []
        for df in self.dfs:
            df = df.select_dtypes(include=['number'])
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
