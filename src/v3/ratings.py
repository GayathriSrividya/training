import pandas as pd
from datetime import datetime

class Ratings:
    ''' 
        Description of class Ratings 
        
        This is a class to manage rows of a pandas Dataframe

        Attributes:
        ----------
        Pandas Dataframe named ratings that contains multiple rows and 13 columns.

        Methods defined here:
        ---------------------
        insert(self, row) 
           input: row
                a dictionary contains 13 arguments 

           output: 
                inserts the arguments into ratings 
        
        read(self, query)
           input: query
                
                query consists of sql query to be executed

            output: 
                executes the sql query and prints status
        
        update(self, const, new_rating)
            input: const, new_rating
                const will be unique value in ratings dataframe
                new_rating is the last updated user rating for the movie

            output: 
                updates the user rating in ratings dataframe with new rating given,
                also changes the date rated wih current date

        delete(self, const)
            input: const

            output: deletes the row in dataframe that matches Const id

    '''
    def __init__(self, ratings):
        '''
            Default Constructor for Ratings

            Parameters:
            ----------
            self, ratings
            ratings is a Pandas Dataframe with multiple rows and 13 columns
            columns include:
            Const 
            Your Rating
            Date Rated
            Title 
            URL
            Title Type
            IMDb Rating
            Runtime (mins)
            Year
            Genres
            Num Votes
            Release Date
            Directors
            
        '''
        self.ratings=ratings

    def update(self, const, new_rating):
        '''
            Summary Line
            Extended description of update(self, const, new_rating)

            parameters:
            -----------
            const 
            new_rating

            selects record in ratings Dataframe that matches const

            checks the validity of the new_rating 
            proceeds with updation only if values ranging between 0 and 10
            
            updates the value of column your_rating with new_rating
            also updates date_rated with current date
            prints the status

            raises exception if any
        '''
        try:
            new_rating=float(new_rating)
            if(new_rating>=0 and new_rating<=10.0):
                date=datetime.now()
                date=date.strftime("%-m/%-d/%Y")
                self.ratings.loc[self.ratings.Const==const, ['Your Rating', 'Date Rated']]=[new_rating, date]
                print("rating updated sucessfully for {0}\n".format(self.ratings.loc[self.ratings.Const==const, 'Title']))
            else:
                print("\ninvalid input!! must be in between 0 and 10!! \nrating not updated\n")
                return -1
        except:
            print("\ninvalid input!! must be in between 0 and 10!! \nrating not updated\n")
            return -1

    def read(self, query):
        '''
            Summary Line 
            Extended Description of read(self, query)

            parameters:
            ----------
            query 

            executes pandas query
            prints the status after each execution

            raises exception if any
        '''
        try:
            if "id" in query:
                id=input("Enter Const id: \n")
            exec(query)
        except:
            print("invalid input\n")
            return -1

    def delete(self, const):
        '''
            Summary Line 
            Extended Description of delete(self, const)

            parameters:
            -----------
            const 

            deletes the row in the Dataframe that matches with const
            prints the status

            raises exception if any
        '''
        try:
            self.ratings.loc[self.ratings.Const==const]
            self.ratings.drop(0, inplace = True)
            print("row deleted from dataframe sucessfully...\n")
        except:
            print("invalid input!")
            return -1

    def insert(self, row):
        '''
            summary line
            extended description of insert(self, row)

            parameters:
            ----------
            row contains 13 arguments
            these 13 arguments holds the information related to movie
            this method when called, inserts/appends the values into ratings dataframe

        '''
        
        try:
            row=pd.DataFrame(row)
            self.ratings=pd.concat([self.ratings, row], axis=0)
            print("row inserted into dataframe successfully...")
        except:
            print("invalid input data!")
            return -1