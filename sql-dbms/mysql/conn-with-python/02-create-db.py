from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        
        with connection.cursor() as cursor:
            create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"
            
            cursor.execute(create_db_query)

        
        with connection.cursor() as cursor:
            show_db_query = "SHOW DATABASES"
            
            cursor.execute(show_db_query)
            
            for db in cursor:
                print(db)

except Error as e:
    print(e)