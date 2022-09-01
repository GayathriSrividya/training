# Below class is to update rating
# Contains functions to update user rating along with current date
# importing necessary modules
import sys
from datetime import datetime

# defining class Ratings

class Ratings:
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

    # function to retrieve rating

    def get_rating(self):
        return self.your_rating

    # this function calls dothis function if rating is in valid range
    # stops execution otherwise

    def set_rating(self, new_rating):
        if(new_rating>=0.0 and new_rating<=10.0):
            self.dothis(new_rating)
        else:
            sys.exit()

    # function to update rating with current date

    def dothis(self,new_rating):
        self.your_rating=new_rating
        day=datetime.now()
        day=day.strftime("%d/%m/%Y")
        self.date_rated=day

