
from Quantaco import settings
import pymysql
import sqlite3

def get_connection(db_path='db.sqlite3', autocommit=True):
    '''Function to set up a connection with the SQLite database.'''
    connection = sqlite3.connect(db_path)
    
    if autocommit:
        connection.isolation_level = None  # This sets autocommit mode

    return connection
