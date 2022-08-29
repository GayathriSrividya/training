# importing required modules

import os
import psycopg2 as ps
import pandas as pd
from config import config
from datetime import datetime

# reading csv file 

print("reading file ratings.csv...\n")
print("converting csv file into pandas dataframe...\n")
df=pd.read_csv("ratings.csv", encoding='latin')
df['Date Rated'] = pd.to_datetime(df['Date Rated'])

# declaring function to insert column values to table

def insert_into_table(cursor, Const, Your_Rating, Date_Rated, Title, URL, Title_Type, IMDb_Rating, Runtime_mins, 
   Year, Genres, Num_Votes, Release_Date, Directors):
   columns=("""INSERT INTO movies (Const, Your_Rating, Date_Rated, Title, URL, Title_type, IMDb_Rating, Runtime_mins, 
   Year, Genres, Num_Votes, Release_Date, Directors) 
   VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""")
   rows=(Const, Your_Rating, Date_Rated, Title, URL, Title_Type, IMDb_Rating, Runtime_mins, Year, 
   Genres, Num_Votes, Release_Date, Directors)
   cursor.execute(columns, rows)
 
# declaring function to append values  

def append_to_db(cursor, df):
   for index, row in df.iterrows():
       insert_into_table(cursor, row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], 
       row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], row['Year'], row['Genres'], row['Num Votes'], 
       row['Release Date'], row['Directors'])
   print("Values are inserted into the database Successfully \n")

# reading the configuration parameters by calling config function

params=config()

# connecting to the postgresql database

conn = ps.connect(**params)
conn.autocommit = True

try:
    
    # declaring a cursor

    cursor = conn.cursor();
    print("Connected to database...\n")

   # deleting the table if already existed in the database 

    cursor.execute("DROP TABLE IF EXISTS movies;")

   # writing a sql query to create table movies 

    create_table = '''CREATE TABLE movies(
    Const VARCHAR(50) NOT NULL,
    Your_Rating FLOAT NOT NULL,
    Date_Rated DATE NOT NULL,
    Title VARCHAR(255) NOT NULL,
    URL VARCHAR(255) NOT NULL,
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

    cursor.execute(create_table);

  # calling append_to_db function to insert values in dataframe to database

    append_to_db(cursor, df)
    conn.commit()
    cursor.execute("SELECT * FROM movies;")

 # closing the cursor

    cursor.close()

except (Exception, ps.DatabaseError) as error:
        print(error)

# closing the database connection

finally:
    if conn is not None:
        conn.close()
        print("Database Connection is closed..")

