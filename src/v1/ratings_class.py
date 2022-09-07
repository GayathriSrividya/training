# importing necessary modules
from datetime import datetime

class Ratings:
    '''
    Description of class Ratings

    This is a class to update user rating and date rated in pandas dataframe

    atrributes:
    -----------
    const       //contains unique id that represents movie
    your_rating //user rating for the movie
    date_rated  //date in which user rating is last updated
    title       //movie title
    url         //url contains link to access the resource
    title_type  //type of movie (eg: movie, short)
    imdb_rating //average rating for the movie
    runtime     //total duration
    year        //year released
    genres      //category of film
    num_votes   //number of votes given
    release_date
    directors   //list of directors

    methods defined here:
    ---------------------
    get_rating(self)
        returns your_rating value

    set_rating(self, new_rating)
        parameters:
         new_rating
         
        updates value in your_rating to new_rating
        updates date_rated to current date

        successful updation depends upon the range in which new_rating lies (0 to 10)


    '''
    def __init__(self, const, your_rating, date_rated, title, url, title_type, imdb_rating, runtime, year, genres, num_votes, release_date, directors):
        '''
        Default Constructor for Ratings class

        parameters:
        -----------
        const
        your_rating
        date_rated
        title
        url
        title_type
        imdb_rating
        runtime
        year
        genres
        num_votes
        release_date
        directors
        '''
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
    
    def get_rating(self, title):
        '''
        Summary Line 
        Extended Description of get_rating(self)

        this method is used to retrieve user rating 
        '''
        if (title==self.title):

            print("your previous rating for "+self.title+":")
            print(self.your_rating)

        else:

            print("title doesn't exist")
            return -1


    def set_rating(self, new_rating):
        '''
        Summary Line 
        Extended Description of set_rating(self, new_rating)

        parameters:
        ----------
        new_rating //input 
        your_rating
        date_rated

        this method is used to update user rating with the input value and also updates the date rated to current date
        the current date will be generated by using folowing commands
            day=datetime.now()
            day=day.strftime("%d/%m/%Y")

        updation will be done only if the input is in valid range i.e, between 0 and 10.0
        stops execution otherwise
        
        '''
        try:
            new_rating=float(new_rating)
            try:
                if(new_rating>=0 and new_rating<=10.0):
                    self.your_rating=new_rating
                    day=datetime.now()
                    day=day.strftime("%d/%m/%Y")
                    self.date_rated=day
                    print("rating updated sucessfully\n")
                else:
                    print("invalid input!! must be in between 0 and 10!! \n \nrating not updated\n")
                    return -1
            except:
                return -1
        except:
            print("invalid input type")
            return -1
