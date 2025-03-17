import sqlite3

def connect_db_movies(db_movies:str):

    conn = sqlite3.connect(db_movies)

    return conn