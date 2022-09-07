import unittest
import json
import sys
from unittest.util import three_way_cmp
sys.path.append('/home/stpl/gayathri/training/src')
from v1.ratings_class import Ratings

class TestRating(unittest.TestCase):
    file_json= open('/home/stpl/gayathri/training/config/v1params.json')
    data = json.load(file_json)
    instance = Ratings("tt0100802", 3, 4/19/2015, "Total Recall", "https://www.imdb.com/title/tt0100802/", "movie", 7.5, 113.0, 1990, "https://www.imdb.com/title/tt0100802/", 278834, "5/31/1990", "Paul Verhoeven")

    def test_set_rating(self):
        for query, text in self.data['set'].items():
            print(query+"\n")
            self.assertEqual(self.instance.set_rating(text[0]), text[1])

    def test_get_rating(self):

        for query, text in self.data['get'].items():
            print(query+'\n')
            self.assertEqual(self.instance.get_rating(text[0]), text[1])
         
if __name__ == '__main__':  
    unittest.main()