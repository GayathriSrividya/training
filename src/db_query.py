import sys
from datetime import datetime
sys.path.append("..")
from utils.dbconfig import dbconfig
import psycopg2 as ps

params=dbconfig()
conn = ps.connect(**params)
conn.autocommit = True

class ManageRecords:
    
    def __init__(self):

        self.cursor=conn.cursor()

        create_table = '''CREATE TABLE IF NOT EXISTS movies(
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
        self.cursor.execute(create_table)

    # method to insert rows into table movies

    def insert(self, row):
        try:
            columns=("""INSERT INTO movies (Const, Your_Rating, Date_Rated, Title, URL, Title_type, IMDb_Rating, Runtime_mins, 
            Year, Genres, Num_Votes, Release_Date, Directors) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""") 
            values=[row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], 
            row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], 
            row['Year'], row['Genres'], row['Num Votes'], row['Release Date'], row['Directors']]
            self.cursor.execute(columns, values)
            conn.commit()
        
        except (Exception, ps.DatabaseError) as error:
            print(error)

    # method to read and return records from table movies

    def read(self, const):
            try:
                query ='''SELECT * FROM movies WHERE Const= %s;'''
                values = [const]
                self.cursor.execute(query, values)
                result=self.cursor.fetchall()
                print(result)
                print("\n")
            except (Exception, ps.DatabaseError) as error:
                print(error)

    # method to update values into the table movies

    def update(self, const, new_rating):
        if (new_rating>0.0 and new_rating<10.0):

            day=datetime.now()
            day=day.strftime("%d/%m/%Y")
            try:
                query = '''UPDATE movies SET Your_Rating = %s, Date_Rated = %s
                WHERE Const = %s;'''
                values=[new_rating, day, const]
                self.cursor.execute(query, values)    
                conn.commit()
                print("values updated in the database successfully...\n")

            except (Exception, ps.DatabaseError) as error:
                print(error)
        else:
            sys.exit("enter a valid value between 0 and 10!!\n")


    # method to delete an existing record from table
        
    def delete(self, const):
        try:
            query='''DELETE FROM movies WHERE Const = %s;'''
            values = [const]
            self.cursor.execute(query, values)
            print("record is deleted from table successfully...\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)