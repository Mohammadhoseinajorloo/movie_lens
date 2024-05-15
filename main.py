from dataset.reader import Reader
from preprocessing import Preprocessing
import pandas as pd

def read_data(filenames):
    movies = Reader(filenames[0]).reader()
    tags = Reader(filenames[1]).reader()
    ratings = Reader(filenames[2]).reader()
    links = Reader(filenames[3]).reader()
    return movies, tags, ratings, links

def preprocessing(dataframe):
    preper_df = Preprocessing(dataframe)
    preper_df.drop_duplicates()
    preper_df.check_missing_data()
    preper_df.find_outliers_IQR(1.5)
    return preper_df


def content_base_approch():
    filenames = ['movies.csv', 'tags.csv', 'ratings.csv', 'links.csv']
    movies, tags, ratings, links = read_data(filenames)
    #--------------------------------------------------
    # Movies
    #--------------------------------------------------
    movies_obj = preprocessing(movies)
    df = movies_obj.content_table(movies['genres'])
    df2 = movies.iloc[:,:2]
    df3 = pd.concat([df2, df], axis=1)
    df3['title'] = df3['title'].apply(lambda x: movies_obj.split_title_year(x)[1])
    df3['years'] = df3['title'].apply(lambda x: movies_obj.split_title_year(x)[0])
    
    print(df3[['title', 'years']])
def main():
    preper_df = content_base_approch()
    return preper_df


if __name__ == "__main__":
    main()


