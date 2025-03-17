import sqlite3

def connect_db(db_movie:str):

    conn = sqlite3.connect(db_movie)

    return conn