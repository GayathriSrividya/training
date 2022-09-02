# importing required modules

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

# this_movie.update('Megamind', 8.2)
# this_movie.update('Megamind', 18.23)
# this_movie.read('Megamind')
# this_movie.delete('Megamind')
# this_movie.read('Megamind')
# this_movie.execute_query()
