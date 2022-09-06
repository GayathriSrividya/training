# importing required modules
import json
import pandas as pd
from records_class import Records

# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("../../data/ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])
print("csv file is successfully converted into dataframe...\n")

# creating instance for ManageRecords class for CRUD operations
 
this_movie=Records()

print("inserting values into database...\n")

for index, row in df.iterrows():
    this_movie.insert(row)

print("Values are inserted into the database Successfully. \n")
this_movie.delete('tt1001526')

file_json= open('../../config/test_query.json')
data = json.load(file_json)
for sqltext in data.values():
    this_movie.read(sqltext, 'tt1001526')

