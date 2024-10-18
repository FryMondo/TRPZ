import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="installation_generator"
    )
    return mydb
