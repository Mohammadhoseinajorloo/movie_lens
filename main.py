from dataset.reader import Reader
from preprocessing import Preprocessing

def content_base_approch(preper_df):
    pass

if __name__ == "__main__":
    movies = Reader('movies.csv').reader().loc[:, ['movieId', 'genres']]
    tags = Reader('tags.csv').reader().loc[:,['userId', 'tag']]
    ratings = Reader('ratings.csv').reader().loc[:, 'rating']
    preper_df = Preprocessing([movies, tags, ratings]).merging()
    print(preper_df)


