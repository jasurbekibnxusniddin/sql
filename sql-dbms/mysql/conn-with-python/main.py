# from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="",
        password="",
        autocommit=True
    ) as connection:
        create_db_query = "CREATE DATABASE online_movie_rating"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)

def ConnWithDB() -> connect:
    try:
        connection = connect(
            host="localhost",
            user="",
            password="",
            use =  "online_movie_rating",
            autocommit=True
        )
        return connection
    except Error as e:
        print(e)

def CreateTables(connection: connect) -> None:
    try:    
        with connection.cursor() as cursor:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS users ( 
                    id INT AUTO_INCREMENT PRIMARY KEY,  
                    username VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """
    except  Error as e:
        print(e) 

def main():
    connection = ConnWithDB()  
    CreateTables(connection)  