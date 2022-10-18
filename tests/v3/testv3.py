import unittest
import json
import pandas as pd
import sys
sys.path.append('../..')
from src.v3.ratings import Ratings

class Testrecords(unittest.TestCase):
    ratings=pd.read_csv('../../data/ratings.csv', encoding='latin')
    instance = Ratings(ratings)  
    file_json= open('../../tests/config/v3params.json')
    data = json.load(file_json)

    def test_insert(self):
        for query, text in self.data['insert'].items():
            print(query+"\n")
            self.assertEqual(self.instance.insert(text[0]), text[1])

    def test_read(self):
        for query, text in self.data['read'].items():
            print(query+"\n")
            self.assertEqual(self.instance.read(text[0]), text[1])
   
    def test_update(self):
        for query, text in self.data['update'].items():
            print(query+"\n")
            self.assertEqual(self.instance.update(text[0], text[1]), text[2])

    def test_delete(self):
        for query, text in self.data['delete'].items():
            print(query+"\n")
            self.assertEqual(self.instance.delete(text[0]), text[1])

if __name__ == '__main__':  
    unittest.main()

