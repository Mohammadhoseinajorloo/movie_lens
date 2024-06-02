from dataset.reader import Reader
from preprocessing import Preprocessing
import pandas as pd

def read_data(filenames):
    movies = Reader(filenames[0]).reader()
    tags = Reader(filenames[1]).reader()
    ratings = Reader(filenames[2]).reader()
    links = Reader(filenames[3]).reader()
    return movies, tags, ratings, links

def preprocessing():
    filenames = ['movies.csv', 'tags.csv', 'ratings.csv', 'links.csv']
    movies, tags, ratings, links = read_data(filenames)

    #--------------------------------------------------
    # Movies
    #--------------------------------------------------
    movies_obj = Preprocessing(movies)
    years, titles = movies_obj.split_title_year(movies, 'title')
    movies['title'] = titles
    movies['years'] = years
    content_table = movies_obj.content_table(movies['genres'])
    df2 = movies[['movieId', 'title', 'years']]
    df3 = pd.concat([df2, content_table], axis=1)
    null_years = movies_obj.year_find(df3[df3['years'].isnull()])
    null_index = df3[df3['years'].isnull()].index
    df3.loc[null_index, 'years'] = null_years
    print(df3.info())


def content_base_approch():
    pass


def main():
    preper_df = preprocessing()
    return preper_df


if __name__ == "__main__":
    main()


