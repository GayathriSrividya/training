# importing required modules
import json

import pandas as pd

from records_class import Records

# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("/home/stpl/gayathri/training/data/ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])
print("csv file is successfully converted into dataframe...\n")
 
# creating instance for Records class
 
this_movie=Records()

print("inserting values into database...\n")

for index, row in df.iterrows():
    this_movie.insert(row)

print("Values are inserted into the database Successfully. \n")

file_json= open('/home/stpl/gayathri/training/config/test_query.json')
data = json.load(file_json)
for query, sqltext in data.items():
    print(query+"\n")
    this_movie.read(sqltext, 'tt1001526')
