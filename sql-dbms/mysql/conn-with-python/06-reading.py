from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="",
        password="",
        database="online_movie_rating",
    ) as connection:
        with connection.cursor() as cursor:
            
            select_movies_query = """
                SELECT 
                    * 
                FROM
                    movies
            """

            cursor.execute(select_movies_query)
            result = cursor.fetchall()
           
            for movie in result:    
                print(movie)
                
except Error as e:
    print(e)