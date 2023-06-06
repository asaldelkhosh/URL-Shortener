import sqlite3
import os
from flask import Flask, render_template, request
import requests
import json

from database.query import Query



# address to sql file
DATABASE_FILE = "./database/sql.db"
API_HOST = "https://yun.ir/api/v1/urls"
API_TOKEN = "1873:b0zc8c1x9m0ococ8ggsowck4ggco08s"


migrate = False # migrate is used in order to create tables
queryParser = Query() # query parser is used to generate sql queries

# create database file
if not os.path.exists(DATABASE_FILE):
  f = open(DATABASE_FILE, "a")
  f.close()
  
  migrate = True


# connect to sqlite database
dbConnection = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
print('[INFO] connection stablished')

# create tables if not exists
if migrate:
  dbConnection.execute(queryParser.createTable())
  dbConnection.execute(queryParser.removeTrigger())
  print('[INFO] migration successed')
  
# create curser for database connection
cur = dbConnection.cursor()


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
  urls = []
  
  # get all urls
  for row in cur.execute(queryParser.getAll()):
    urls.append(row)
  
  return {
    'urls': urls
  }
  

@app.route("/url", methods=['POST']) # create a new url
def createURL():
  # get request content
  content = request.get_json(silent=True)
  
  row = cur.execute(queryParser.getURL(content['url']))
  if len(row) > 0:
    return row['short']
  
  title = content['url'].replace("http://", "").replace("https://", "")
  
  data = {
    "title": title,
    "url": content['url'],
  }
  
  headers = {
    'Content-Type': 'application/json',
    'X-API-Key': API_TOKEN,
  }
  
  res = requests.post(API_HOST, data=json.dumps(data), headers=headers)
  resJSON = res.json()
  
  # save it into database
  cur.execute(queryParser.createURL(content['url'], resJSON['doc']['url']))
  dbConnection.commit()
  
  return resJSON['doc']['url']
  

@app.route("/url/<id>", methods=['GET']) # remove an url
def deleteURL(id):
  # remove url by id
  cur.execute(queryParser.removeURL(int(id)))
  dbConnection.commit()
  
  return 'OK'


@app.route("/url/<id>", methods=['POST']) # update an url
def updateURL(id):
  cur.execute(queryParser.updateURL(int(id)))
  dbConnection.commit()
  
  return 'OK'


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)
