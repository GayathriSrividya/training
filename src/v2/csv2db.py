# importing required modules
import json

import pandas as pd

from records import Ratings


# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("../../data/ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])
print("csv file is successfully converted into dataframe...\n")
 
# creating instance for Ratings class
 
this_title=Ratings()

print("inserting values into database...\n")

for index, row in df.iterrows():
    this_title.insert(row)

print("Values are inserted into the database Successfully. \n")

read_queries= open('../../config/read_queries.json')
query_data = json.load(read_queries)
for query, sqltext in query_data.items():
    print(query+"\n")
    this_title.read(sqltext, 'tt1001526')
    
this_title.update("tt1001526", 7.23)
this_title.delete("tt1001526")