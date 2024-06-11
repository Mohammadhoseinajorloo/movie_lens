import pandas as pd
import streamlit as st
import os
import requests

####################
#####Constanses#####
####################

DATA_PATH = os.path.abspath("data")
FILES = os.listdir(DATA_PATH)

MOVIES_PATH = os.path.join(DATA_PATH, FILES[0])
RATINGS_PATH = os.path.join(DATA_PATH, FILES[1])
TAGS_PATH = os.path.join(DATA_PATH, FILES[2])
LINKS_PATH = os.path.join(DATA_PATH, FILES[3])

############################
########Fetch Poster########
############################

def fetch_poster(movieid):
    api = "https://api.themoviedb.org/3/movie/" + str(movieid) + "?api_key=4c66f711cd0eece2baa79637c2d7fd94"
    resopnse = requests.get(api)
    if resopnse.status_code == 200:
        json = resopnse.json()
        return "https://image.tmdb.org/t/p/w500" + json["poster_path"]

###################################
########Simple Recommenders########
###################################

def simple_recommenders(n=5):
    '''
    Simple recommenders: offer generalized recommendations to every user, based on movie popularity and/or genre. The basic idea behind this system is that movies that are more popular and critically acclaimed will have a higher probability of being liked by the average audience. An example could be IMDB Top 250.
    ===
    parameters:
    1. n (int)[defult=5]
        number of top movies
    '''
    recommenders_movies = []
    recommenders_poster = []

    movies = pd.read_csv(MOVIES_PATH)
    ratings = pd.read_csv(RATINGS_PATH)
    links = pd.read_csv(LINKS_PATH)

    ratings["title"] = ratings["movieId"].map(movies.set_index("movieId")["title"])
    ratings["poster"] = ratings["movieId"].map(links.set_index("movieId")["tmdbId"])

    sorted_ratings = ratings.sort_values(by=["rating"], ascending=False).reset_index(drop=True)

    top_five = sorted_ratings[:n]

    for i in top_five.values:
        recommenders_movies.append(i[-2])
        recommenders_poster.append(fetch_poster(i[-1]))

    return recommenders_movies, recommenders_poster


#########################################
########Content_Base_Recommenders########
#########################################
def content_base_recommenders(movie):
    """
    suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person likes a particular item, he or she will also like an item that is similar to it. And to recommend that, it will make use of the user's past item metadata. A good example could be YouTube, where based on your history, it suggests you new videos that you could potentially watch.
    ===
    parameters:
    1. movie (str)
        name movie for recommender
    """
    pass

####################
########Main########
####################
if __name__ == "__main__":
    st.write("# Simple Recommender")
    recommenders_movies, recommenders_poster = simple_recommenders()
    col1, col2, col3, col4, col5 = st.columns(5, gap="medium")
    with col1:
        st.text(recommenders_movies[0])
        st.image(recommenders_poster[0])
    with col2:
        st.text(recommenders_movies[1])
        st.image(recommenders_poster[1])
    with col3:
        st.text(recommenders_movies[2])
        st.image(recommenders_poster[2])
    with col4:
        st.text(recommenders_movies[3])
        st.image(recommenders_poster[3])
    with col5:
        st.text(recommenders_movies[4])
        st.image(recommenders_poster[4])
