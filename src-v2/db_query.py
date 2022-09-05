# import required dependencies

import sys
from datetime import datetime
sys.path.append("..")
from utils.dbconfig import dbconfig
import json
import psycopg2 as ps

# arranging connection to postgresql database

params=dbconfig()
conn = ps.connect(**params)
conn.autocommit = True

class ManageRecords:
    ''' 
        Description of class ManageRecords 
        
        This is a class to managerecords of a postgreSQL table

        Attributes:
        ----------
        Table named movies that contains multiple records.

        Methods defined here:
        ---------------------
        insert(self, row) 
           input: row 
                row contains 13 arguments that have information about movie

           output: 
                inserts the arguments into movies table 
        
        read(self, title)
           input: title 
                title is primary key in movies table

            output: 
                prints record in the movies table that matches the argument title 
        
        update(self, title, new_rating)
            input: title, new_rating
                title is the primary key in movies table
                new_rating is the last updated user rating for the movie

            output: 
                updates the user rating in movies table with new rating given,
                also changes the date rated wih current date

        delete(self, title)
            input: title

            output: deletes the user rating in the record that matches title

        execute_query(self)
            reads the json file with SQL queries
            this method when called executes the queries and prints the status
    '''
    def __init__(self):
        '''
        Default constructor for ManageRecords
        creates a table named movies, along with 13 columns namely
            Const
            Your_Rating
            Date_Rated
            Title // primary key
            URL
            Title_Type
            IMDb_Rating
            Runtime_mins
            Year
            Genres
            Num_Votes
            Release_date
            Directors

        '''
        self.cursor=conn.cursor()

        create_table = '''CREATE TABLE IF NOT EXISTS movies(
                        Const VARCHAR(50) NOT NULL,
                        Your_Rating FLOAT NOT NULL,
                        Date_Rated DATE NOT NULL,
                        Title VARCHAR(255) NOT NULL PRIMARY KEY,
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

    def insert(self, row):
        '''
        summary line
        extended description of inser(self, row)

        parameters:
        ----------
        row contains 13 arguments
        these 13 arguments holds the information related to movie
        this method when called, inserts the values into movies table 

        '''
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

    def read(self, title):
        '''
        Summary Line 
        Extended Description of read(self, title)

        parameters:
        ----------
        title // primary key in the table movies

        returns record from the table that matches the title

        raises exception if any

        '''
        try:
            query ='''SELECT * FROM movies WHERE Title= %s;'''
            values = [title]
            self.cursor.execute(query, values)
            result=self.cursor.fetchall()
            print(result)
            print("\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)

    def update(self, title, new_rating):
        '''
        Summary Line
        Extended description of update(self, title, new_rating)

        parameters:
        -----------
        title //primary key
        new_rating

        selects record in movies table that matches title 

        checks the validity of the new_rating 
        proceeds with updation only if values ranging between 0 and 10
        
        updates the value of column your_rating with new_rating
        also updates date_rated with current date
        prints the status

        raises exception if any
        '''
        if (new_rating>0.0 and new_rating<10.0):

            day=datetime.now()
            day=day.strftime("%d/%m/%Y")
            try:
                query = '''UPDATE movies SET Your_Rating = %s, Date_Rated = %s
                WHERE Title = %s;'''
                values=[new_rating, day, title]
                self.cursor.execute(query, values)    
                conn.commit()
                print("values updated in the database successfully...\n")

            except (Exception, ps.DatabaseError) as error:
                print(error)
        else:
            sys.exit("enter a valid value between 0 and 10!!\n")
        
    def delete(self, title):
        '''
        Summary Line 
        Extended Description of delete(self, title)

        parameters:
        -----------
        title //primary key

        selects the rating in the record that matches with title 
        sets the rating to 0
        prints the status

        raises exception if any
        '''
        try:
            query='''UPDATE movies SET Your_Rating = %s WHERE Title = %s;'''
            values = [0, title]
            self.cursor.execute(query, values)
            print("rating is deleted from record successfully...\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)
            
    def execute_query(self):
        '''
        Sumamry Line 
        EXtended Description of execute_query(self)

        this method when called 
            reads json file from the given path
            the json file contains SQL queries
            this method loads the queries and executes them
            prints the status by executing queries one by one
        '''
        file_json= open('../json/test_query.json')
        data = json.load(file_json)
        for sqltext in data.values():
            self.cursor.execute(sqltext)
            result = self.cursor.fetchall()
            print(result)
            print("\n")
