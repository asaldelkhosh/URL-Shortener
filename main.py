import sqlite3
import os
from flask import Flask, render_template, request

from database.query import Query



# address to sql file
DATABASE_FILE = "./database/sql.db"


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
app = Flask(__name__,
            static_url_path='/', 
            static_folder='web/static',
            template_folder='web/template')


# creating http routes

@app.route("/") # return the home page
def index():
  return render_template('index.html')

@app.route("/url", methods=['GET']) # return all of the urls
def getURLs():
  cur = dbConnection.cursor()
  urls = []
  
  # get all urls
  for row in cur.execute(queryParser.getAll()):
    urls.append(row)
    
  cur.close()
  
  return urls
  

@app.route("/url", methods=['POST']) # create a new url
def createURL():
  # get request content
  content = request.get_json(silent=True)
  
  # save it into database
  cur = dbConnection.cursor()
  cur.execute(queryParser.createURL(content['url'], content['url']))
  cur.close()
  
  return 'OK'
  

@app.route("/url/<id>", methods=['POST']) # remove an url
def deleteURL(id):
  # remove url by id
  cur = dbConnection.cursor()
  cur.execute(queryParser.removeURL(int(id)))
  cur.close()
  
  return 'OK'



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)
