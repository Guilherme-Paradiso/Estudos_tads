import sqlite3

def connect_db(db_name:str):
    """
    
    Connect to an existent data base.
    If not exist, it will create one.

    args
        db_name (str): A database name. 
    """

    conn = sqlite3.connect(db_name)

    return conn