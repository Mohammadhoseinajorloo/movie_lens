# First createing virtual envierment for project 
# We for this project use from 'virtualenv' | file-name : .env 

# import depensensies
import pandas as pd 
    


if __name__ == '__main__':

    genome_scores_path = './data/genome-scores.csv'
    genome_tags_path = './data/genome-tags.csv'
    links_path = './data/links.csv'
    movies_path = './data/movies.csv'
    ratings_path = './data/ratings.csv'
    tags_path = './data/tags.csv'
    
    genome_scores_dataset = pd.read_csv(genome_scores_path)
    genome_tags_dataset = pd.read_csv(genome_tags_path)
    links_dataset = pd.read_csv(links_path)
    movies_dataset = pd.read_csv(movies_path)
    ratings_dataset = pd.read_csv(ratings_path)
    tags_dataset = pd.read_csv(tags_path)
