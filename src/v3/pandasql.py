# importing required modules
import pandas as pd

import json

from ratings import Ratings

 
# reading csv file 
ratings=pd.read_csv('../../data/ratings.csv', encoding='latin')

# reading json file contains pandas queries

panda_queries=open('../../config/panda_queries.json')
query_data=json.load(panda_queries)

# creating instance for Ratings class

this_title=Ratings(ratings)

# executing pandas queries one by one

for query, pdtxt in query_data.items():
    print(query+':\n')
    this_title.read(pdtxt)


this_title.update('tt1001526', 7.23)
this_title.delete('tt1013753')
new_row={'Const':['tt1001526'],'Your Rating': [6],'Date Rated':['3/18/2017'],'Title':['Megamind'],'URL':['https://www.imdb.com/title/tt1001526/'],'Title Type':['movie'],'IMDb Rating':['7.3'],'Runtime (mins)':[95],'Year':[2010],'Genres':['Animation, Action, Comedy, Family, Sci-Fi'],'Num Votes':[208264],'Release Date':['10/28/2010'],'Directors':['Tom McGrath']}
this_title.insert(new_row)