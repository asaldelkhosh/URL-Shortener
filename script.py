import sqlite3
import os
from flask import Flask

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
print('[INFO] connection stablished')

# create tables if not exists
if migrate:
  dbConnection.execute(queryParser.createTable())
  print('[INFO] migration successed')


# create a new flask app
app = Flask(__name__)



# creating http routes

@app.route("/") # return the home page
def index():
  pass

@app.route("/url", methods=['GET']) # return all of the urls
def getURLs():
  pass

@app.route("/url", methods=['POST']) # create a new url
def createURL():
  pass

@app.route("/url/<id>", methods=['POST']) # remove an url
def deleteURL():
  pass



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)
