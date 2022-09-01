# importing required modules

import os
import psycopg2 as ps
import pandas as pd
from config import config
from crudclass import CrudOnDatabase
from datetime import datetime


# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("../data/ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])

# reading the configuration parameters by calling config function

params=config()

# connecting to the postgresql database

conn = ps.connect(**params)
conn.autocommit = True

try:
    
    # declaring a cursor

    cursor = conn.cursor()
    print("Connected to database...\n")

   # deleting the table if already existed in the database 

    cursor.execute("DROP TABLE IF EXISTS movies;")

   # writing a sql query to create table movies 

    create_table = '''CREATE TABLE movies(
    Const VARCHAR(50) NOT NULL PRIMARY KEY,
    Your_Rating FLOAT NOT NULL,
    Date_Rated DATE NOT NULL,
    Title VARCHAR(255) NOT NULL,
    URL VARCHAR(50) NOT NULL,
    Title_Type VARCHAR(50) NOT NULL,
    IMDb_Rating VARCHAR(50) NOT NULL,
    Runtime_mins FLOAT NOT NULL,
    Year INT NOT NULL,
    Genres VARCHAR(255) NOT NULL,
    Num_Votes INT NOT NULL,
    Release_date VARCHAR(50) NOT NULL,
    Directors VARCHAR(255) NOT NULL
    )'''

   # executing the query
   # after successful execution a table named movies will be created in the database

    cursor.execute(create_table)
    print("inserting values into database...\n")
    for i, row in df.iterrows():
        # creating class instance to handle CRUD functions on database
         
        this_movie = CrudOnDatabase(row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], row['Year'], row['Genres'], row['Num Votes'], row['Release Date'], row['Directors'])
        this_movie.insert()
    print("Values are inserted into the database Successfully \n")

    # commiting the changes

    conn.commit()

    # closing the cursor

    cursor.close()

# exception block print the error if any

except (Exception, ps.DatabaseError) as error:
        print(error)

# closing the database connection

finally:
    if conn is not None:
        conn.close()
        print("Database Connection is closed...\n")


# below statements are examples how to call crud functions using class instance

# this_movie.update('tt1001526', 8.23)
# this_movie.update('tt1001526', 18.23)
# this_movie.read('tt1001526')
# this_movie.delete('tt1001526')
