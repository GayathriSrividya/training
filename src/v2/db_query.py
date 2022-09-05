# import required dependencies
from datetime import datetime
import sys
sys.path.append("../..")
from utils.dbconfig import dbconfig
import psycopg2 as ps

class ManageRecords:
    ''' 
        Description of class ManageRecords 
        
        This is a class to managerecords of a postgreSQL table

        Attributes:
        ----------
        Table named ratings that contains multiple records.

        Methods defined here:
        ---------------------
        insert(self, row) 
           input: row 
                row contains 13 arguments that have information about movie

           output: 
                inserts the arguments into ratings table 
        
        read(self, const)
           input: const
                const is primary key in ratings table

            output: 
                prints record in the movies table that matches the argument title 
        
        update(self, const, new_rating)
            input: const, new_rating
                const is the primary key in ratings table
                new_rating is the last updated user rating for the movie

            output: 
                updates the user rating in ratings table with new rating given,
                also changes the date rated wih current date

        delete(self, const)
            input: const

            output: deletes the user rating in the record that matches title

    '''
    def __init__(self):
        '''
        Default constructor for ManageRecords
        creates a table named ratings, along with 13 columns namely
            Const // primary key
            Your_Rating
            Date_Rated
            Title 
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
        params=dbconfig()
        self.conn = ps.connect(**params)
        self.conn.autocommit = True
        self.cursor=self.conn.cursor()

        create_table = '''CREATE TABLE IF NOT EXISTS ratings(
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

    def insert(self, row):
        '''
        summary line
        extended description of insert(self, row)

        parameters:
        ----------
        row contains 13 arguments
        these 13 arguments holds the information related to movie
        this method when called, inserts the values into ratings table 

        '''
        try:
            columns=("""INSERT INTO ratings (Const, Your_Rating, Date_Rated, Title, URL, Title_type, IMDb_Rating, Runtime_mins, 
            Year, Genres, Num_Votes, Release_Date, Directors) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""") 
            values=[row['Const'], row['Your Rating'], row['Date Rated'], row['Title'], row['URL'], 
            row['Title Type'], row['IMDb Rating'], row['Runtime (mins)'], 
            row['Year'], row['Genres'], row['Num Votes'], row['Release Date'], row['Directors']]
            self.cursor.execute(columns, values)
            self.conn.commit()
        
        except (Exception, ps.DatabaseError) as error:
            print(error)

    def read(self, query, params):
        '''
        Summary Line 
        Extended Description of read(self, query, params)

        parameters:
        ----------
        query 
        params

        executes sql query along with params if exists
        prints the status after each execution

        raises exception if any
        '''
        try:
            values =[params]
            self.cursor.execute(query, values)
            result=self.cursor.fetchall()
            print(result)
            print("\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)

    def update(self, const, new_rating):
        '''
        Summary Line
        Extended description of update(self, const, new_rating)

        parameters:
        -----------
        const //primary key
        new_rating

        selects record in ratings table that matches title 

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
                query = '''UPDATE ratings SET Your_Rating = %s, Date_Rated = %s
                WHERE Const = %s;'''
                values=[new_rating, day, const]
                self.cursor.execute(query, values)    
                self.conn.commit()
                print("values updated in the database successfully...\n")

            except (Exception, ps.DatabaseError) as error:
                print(error)
        else:
            sys.exit("enter a valid value between 0 and 10!!\n")
        
    def delete(self, const):
        '''
        Summary Line 
        Extended Description of delete(self, const)

        parameters:
        -----------
        const //primary key

        selects the rating in the record that matches with title 
        sets the rating to 0
        prints the status

        raises exception if any
        '''
        try:
            query='''UPDATE ratings SET Your_Rating = %s WHERE Const = %s;'''
            values = [0, const]
            self.cursor.execute(query, values)
            print("rating is deleted from record successfully...\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)
            
