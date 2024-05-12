from dataset.reader import Reader
from preprocessing import Preprocessing

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
    movies = preprocessing(movies)
    return movies 

def main():
    preper_df = content_base_approch()
    return preper_df


if __name__ == "__main__":
    main()


