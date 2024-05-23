import mysql.connector

def get_connection():
    try:
        return mysql.connector.connect(
            host="root",
            user="root",
            password="@1502",
            database="tienda"
        )
    except mysql.connector.Error as err: 
        raise err 
