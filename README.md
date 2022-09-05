This repo is for training on Python.

The data folder contains a ratings.csv file. The file has the following columns:
Const,Your Rating,Date Rated,Title,URL,Title Type,IMDb Rating,Runtime (mins),Year,Genres,Num Votes,Release Date,Directors

1) Create a Class with the above listed properties. 
  - The required fields should be listed static.
  - There should be get and set methods.
  - There should be a function to update Your Rating.
  - Updating Your Rating should also update Date Rated internally.

2) Programatically read the CSV file
3) Iterate through the contents of the CSV file and for each row
4) Create a new instance of above class. 

###########################################

* Create a virtual environment
* Create a requirements.txt file with required dependencies
* Create a .gitignore file
* Create a Unit test case
* Generate test coverage

###########################################

* Clone the repository to your own
* Create a new branch
* Every commit should be GPG signed
* Create a Pull Request with updated code

###########################################

this repo contains following folders

data:
----
  data consists of ratings.csv file

config:
------
  test_query.json // json file that consists of SQL queries

utils:
-----

  dbconfig.py     // python file used for configuration of postgreSQL server

src:
----
src folder consists of python programs that retrieve and manipulate values in csv file using
pandas and postgreSQL

src->v1
-------
.update_ratings.py ---- this file has set of instructions that converts csv file to pandas dataframe, creates instance for the class 				 	Ratings to retrieve and update user rating

.ratings_class.py ----- this python class contains dataframe values as attributes also 	consists of methods get_rating(), set_rating() to 				 update user rating along with current date

src->v2
------
.df_to_db.py  ---- converts csv file to postgreSQL using pandas, creating instance for the class ManageRecords to manipulate columns in the 
		  postgreSQL table
		  
.db_query.py ---- consists of python class ManageRecords, involves different methods 
		  to create a table and also perform CRUD(create, read, update, delete) operations on the table 
