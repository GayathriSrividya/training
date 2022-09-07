import unittest
import json
import sys
sys.path.append("/home/stpl/gayathri/training/src")
from v2.records_class import Records

class Testrecords(unittest.TestCase):

    instance = Records()  
    file_json= open('/home/stpl/gayathri/training/config/v2params.json')
    data = json.load(file_json)

    def test_insert(self):
        for query, text in self.data['insert'].items():
            print(query+"\n")
            self.assertEqual(self.instance.insert(text[0]), text[1])

    def test_read(self):
        for query, text in self.data['read'].items():
            print(query+"\n")
            self.assertEqual(self.instance.read(text[0], text[1]), text[2])
   
    def test_update(self):
        for query, text in self.data['update'].items():
            print(query+"\n")
            self.assertEqual(self.instance.update(text[0], text[1]), text[2])

    def test_delete(self):
        for query, text in self.data['delete'].items():
            print(query+"\n")
            self.assertEqual(self.instance.delete(text[0]), text[1])
            
unittest.main()