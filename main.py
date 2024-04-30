from constants import *
from dataset import Dataset

# 1. anonymization
# 2. how to evaluate a model : train-validation split
#   timestamp -> date time
# 3. Data Cleaning
# Number of unique keys per table (e.g. unique attendees in attendee)
#Number of duplicated keys per table
#% of matches between two tables (e.g. can we link all gtc_talks_catalog keys in attendee_attendance to gtc_talks_catalog
#Number of gtc_talks_catalog per GTC Event
#Number of attendee_attendance per GTC Event
#Number of watched GTC talks per attendee etc.
# 4. Feature Validation and Selection
#Calculate the % of NaN per features (how many rows do miss the feature)
#Calculate the % of NaN per GTC event per features
#Is the feature a categorical attribute (e.g. country) or numeric attribute (e.g. video length)?
#For each categorical attribute:
#What is the distribution of categories?
#How many unique values?
#For each numerical attribute:
#What is the distribution?
# 5. More Data Cleaning

class Preprocessing:
    def __init__(self, dataset):
        self.dataset = dataset

    def drop_nulls(self):
        pass

if __name__ == '__main__':
    dataset = Dataset(PATH)
    dataset = Preprocessing(dataset)
    print(dataset)
