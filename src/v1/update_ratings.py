# import necessary packages
import sys
from ratings_class import Ratings
import pandas as pd

# Read the csv file
# Load the CSV into a Data Frame

csv_file=pd.read_csv('../data/ratings.csv', encoding='latin')

# iterating over the Data Frame rows using df.iterrows()

for index, row in csv_file[0:10].iterrows():

    # reading the input

    my_rating=input("\n"+"YOUR RATING FOR:  "+ row["Title"]+"\n")
    
    # checking the rating is valid type


    try:
        my_rating=float(my_rating)
        # Create object this_movie for Ratings class

        this_movie =Ratings(row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], row['Year'], row['Genres'], row['Num Votes'], row['Release Date'], row['Directors'])

        # Calling set_rating method

        this_movie.set_rating(my_rating)

    # if input is invalid exit the code

    except:

        sys.exit("Enter value between 0 and 10 only!")

