import sqlite3
import os



# address to sql file
DATABASE_FILE = "sql.db"


# create database file
if not os.path.exists(DATABASE_FILE):
  f = open(DATABASE_FILE, "a")
  f.close()


# connect to sqlite database
dbConnection = sqlite3.connect(DATABASE_FILE)
