# import necessary packages
import pandas as pd
from ratings_class import Ratings
# Read the csv file
# Load the data in csv file into a Data Frame

csv_file=pd.read_csv('/home/stpl/gayathri/training/data/ratings.csv', encoding='latin')

# iterating over the Data Frame rows using df.iterrows()

for index, row in csv_file[0:10].iterrows():

        #creating instance for class Ratings
        
        this_movie =Ratings(row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], row['Year'], row['Genres'], row['Num Votes'], row['Release Date'], row['Directors'])
    