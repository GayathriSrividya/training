import sys
from datetime import datetime
from config import config
import psycopg2 as ps

params=config()
conn = ps.connect(**params)
conn.autocommit = True
cursor=conn.cursor()


class CrudOnDatabase:
    
    
    def __init__(self, const, your_rating, date_rated, title, url, title_type, imdb_rating, runtime, year, genres, num_votes, release_date, directors):
      
        self.const=const
        self.your_rating=your_rating
        self.date_rated=date_rated
        self.title=title
        self.url=url
        self.title_type=title_type
        self.imdb_rating=imdb_rating
        self.runtime=runtime
        self.year=year
        self.genres=genres
        self.num_votes=num_votes
        self.release_date=release_date
        self.directors=directors

    # method to insert rows into table movies

    def insert(self):
        
        try:
            columns=("""INSERT INTO movies (Const, Your_Rating, Date_Rated, Title, URL, Title_type, IMDb_Rating, Runtime_mins, 
            Year, Genres, Num_Votes, Release_Date, Directors) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""") 
            values=[self.const, self.your_rating, self.date_rated,
            self.title, self.url, self.title_type, self.imdb_rating, self.runtime, self.year, self.genres, self.num_votes, self.release_date, self.directors]
            cursor.execute(columns, values)
            conn.commit()
        
        except (Exception, ps.DatabaseError) as error:
            print(error)

    # method to read and return records from table movies

    def read(self, const):
            try:
                query ='''SELECT * FROM movies WHERE Const= %s;'''
                values = [const]
                cursor.execute(query, values)
                result=cursor.fetchall()
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
                cursor.execute(query, values)    
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
            cursor.execute(query, values)
            print("record is deleted from table successfully...\n")
        except (Exception, ps.DatabaseError) as error:
            print(error)