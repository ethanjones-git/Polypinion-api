import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='dvp',
    password='Zzb33k23432@#$#@',
    database='test'
)

if connection.is_connected():
    print("Connected to MySQL database")

connection.close()
