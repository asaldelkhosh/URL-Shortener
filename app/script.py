import sqlite3
import os

from query import Query



# address to sql file
DATABASE_FILE = "sql.db"


migrate = False # migrate is used in order to create tables
queryParser = Query() # query parser is used to generate sql queries

# create database file
if not os.path.exists(DATABASE_FILE):
  f = open(DATABASE_FILE, "a")
  f.close()
  
  migrate = True


# connect to sqlite database
dbConnection = sqlite3.connect(DATABASE_FILE)

# create tables if not exists
if migrate:
  dbConnection.execute(queryParser.createTable())
