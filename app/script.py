import mysql.connector



# connect to mysql
dbConnection = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
