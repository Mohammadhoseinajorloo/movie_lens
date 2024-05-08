from dataset.reader import Reader
from preprocessing import Preprocessing

def read_data(filenames):
    movies = Reader(filenames[0]).reader().loc[:, ['movieId', 'genres']]
    tags = Reader(filenames[1]).reader().loc[:,['userId', 'tag']]
    ratings = Reader(filenames[2]).reader().loc[:, 'rating']
    return list(movies, tags, ratings)

def preprocessing(dataframes):
    preper_df = Preprocessing(dataframes)
    preper_df = preper_df.merging()
    return preper_df


def content_base_approch():
    filenames = ['links.csv', 'movies.csv', 'ratings.csv']
    dataframes = read_data(filenames)
    preper_df = preprocessing(dataframes)
    return preper_df

def main():
    preper_df = content_base_approch()
    print(preper_df)


if __name__ == "__main__":
    main()


