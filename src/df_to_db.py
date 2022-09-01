# importing required modules

import psycopg2 as ps
import pandas as pd
from db_query import ManageRecords

# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("../data/ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])
print("csv file is successfully converted into dataframe...\n")

# creating instance for ManageRecords class for CRUD operations

this_movie=ManageRecords()

print("inserting values into database...\n")

for index, row in df.iterrows():
    this_movie.insert(row)

print("Values are inserted into the database Successfully. \n")









# below statements are examples how to call crud functions using class instance

# this_movie.update('tt1001526', 8.23)
# this_movie.update('tt1001526', 18.23)
# this_movie.read('tt1001526')
# this_movie.delete('tt1001526')
