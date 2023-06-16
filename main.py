import sqlite3
import os
import requests
import json

from flask import Flask, render_template, request
from datetime import datetime

from database.query import Query



# address to sql file
DATABASE_FILE = "./database/sql.db"
API_HOST = os.getenv("API_HOST")
API_TOKEN = os.getenv("API_TOKEN")


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
  dbConnection.execute(queryParser.getAllView())
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


@app.route("/history") # return the history page
def history():
  return render_template('history.html')


@app.route("/history/data", methods=['GET']) # get all of the urls with history
def getHistoryData():
  # create curser for database connection
  cur = dbConnection.cursor()

  urls = []
  
  # get all urls
  for row in cur.execute(queryParser.getAllByDate()):
    urls.append(row)
  
  cur.close()
  
  return {
    'urls': urls
  }


@app.route("/url", methods=['GET']) # return all of the urls
def getURLs():
  # create curser for database connection
  cur = dbConnection.cursor()

  urls = []
  
  # get all urls
  for row in cur.execute(queryParser.getAll()):
    urls.append(row)
  
  cur.close()
  
  return {
    'urls': urls
  }
  

@app.route("/url", methods=['POST']) # create a new url
def createURL():
  # create curser for database connection
  cur = dbConnection.cursor()
  
  # get request content
  content = request.get_json(silent=True)
  
  cur.execute(queryParser.getURL(), [content['url']])
  
  # if data already exists
  data = cur.fetchone()
  if data != None:
    cur.execute(queryParser.updateURL(), [datetime.now(), data[0]])
    dbConnection.commit()
    
    cur.close()
     
    return data[2]
  
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
  
  time = datetime.now()
  
  # save it into database
  cur.execute(queryParser.createURL(), [content['url'], resJSON['doc']['url'], 1, time, time])
  dbConnection.commit()
  
  cur.close()
  
  return resJSON['doc']['url']
  

@app.route("/url/<id>", methods=['GET']) # remove an url
def deleteURL(id):
  # create curser for database connection
  cur = dbConnection.cursor()
  
  # remove url by id
  cur.execute(queryParser.removeURL(), [int(id)])
  dbConnection.commit()
  
  cur.close()
  
  return 'OK'


@app.route("/url/<id>", methods=['POST']) # update an url
def updateURL(id):
  # create curser for database connection
  cur = dbConnection.cursor()
  
  cur.execute(queryParser.updateURL(), [datetime.now(), int(id)])
  dbConnection.commit()
  
  cur.close()
  
  return 'OK'


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000)
