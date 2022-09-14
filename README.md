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
  read_queries.json // json file that consists of SQL queries
  pandas_queries.json // json file consists of pandas commands

utils:
-----

  dbconfig.py     // python file used for configuration of postgreSQL server

src:
----
src folder consists of python programs that retrieve and manipulate values in csv file using
pandas and postgreSQL

src->v1
-------
1)csv2pandas.py ---- this file has set of instructions that converts csv file to pandas dataframe, creates instance for the class 				 	Ratings to retrieve and update user rating

2)ratings.py ----- this python class contains dataframe values as attributes also 	consists of methods get_rating(), set_rating() to update user rating along with current date

src->v2
------
1)csv2db.py  ---- converts csv file to postgreSQL using pandas, creating instance for the class Ratings to manipulate columns in the 
		  postgreSQL table
		  
2)ratings.py ---- consists of python class Ratings, involves different methods 
		  to create a table and also perform CRUD(create, read, update, delete) operations on the table 

src->v3
------
1)pandasql.py  ---- converts csv file pandas Dataframe, creating instance for the class Ratings to manipulate columns in the Dataframe
		  
2)ratings.py ---- consists of python class Ratings, involves different methods 
		  to create a table and also perform CRUD(create, read, update, delete) operations on the Dataframe

tests:
------

this folder contains unittest files to check functionality of python codes existing in src folder, and also contains json files containing test cases.

tests->config
-------------

this folder consists of json files which have parameters for the test cases

setting up github repository:
----------------------------

Before you start working on the project, create your own github repository and generate SSH, GPG keys for authentication.
for more information, refer below:


https://docs.github.com/en/get-started/quickstart/create-a-repo

https://docs.github.com/en/authentication/connecting-to-github-with-ssh

https://docs.github.com/en/authentication/managing-commit-signature-verification


create python virtual environment in your linux system
----------------------------------------------------- 

run python -V (if version is not displayed run sudo apt install python3)

after installing python, run "python -m venv my-project-env" 

then virtual environment named my-project-env will be created. 

run "source my-project-env/bin/activate" to activate 

run "pip install requests" & "python -c "import requests"" only for the first time.

to close the virtual environment, type "deactivate"


install postgres in linux:
--------------------------

type the following command 

"sudo apt-get install postgresql"

after successful installation, connect to postgresql using 
"sudo -i -u postgres"

the user will now switched to postgres, type "psql" to connect with database server or to return to regular user type "exit" or press ctrl+d

postgres@user:~$ psql

postgres=# // here you can create different databases and manage tables 

to create a database
postgres=# "create database my_database;"

connect to database "my_database"
postgres=# \c my_database

to exit type \q or ctrl+d


setup:
-----
install required dependencies in requirements.txt file

"pip install -r requirements.txt"

create a new directory using "mkdir dir_name"

to navigate into directory use "cd path/to/dir_name"

create a new file (say python file) use "touch file.py"

to execute a python script, use command "python file.py" or "python path/to/file.py"

Generate test coverage:
-----------------------

type the following commands in the terminal to generate test coverage report

"coverage run -m unittest discover"

"coverage report"

"coverage html"