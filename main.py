from dataset.reader import Reader
from preprocessing import Preprocessing

def read_data(filenames):
    movies = Reader(filenames[0]).reader()
    tags = Reader(filenames[1]).reader()
    ratings = Reader(filenames[2]).reader()
    return list((movies, tags, ratings))

def preprocessing(dataframes):
    preper_df = Preprocessing(dataframes)
    preper_df.drop_duplicates()
    preper_df.check_missing_data()
    print(preper_df.find_outliers_IQR(1.5))
    return preper_df


def content_base_approch():
    filenames = ['movies.csv', 'tags.csv', 'ratings.csv']
    dataframes = read_data(filenames)
    preper_df = preprocessing(dataframes)
    return preper_df

def main():
    preper_df = content_base_approch()
    return preper_df


if __name__ == "__main__":
    main()


