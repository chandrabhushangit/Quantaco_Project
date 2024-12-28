
from Quantaco import settings
import sqlite3
def get_connection(autocommit=True):
    '''Function to set up a connection with the database. Pass 'False' as an argument if autocommit is to be disabled.'''
    # connection = pymysql.connect(host=settings.DATABASES['default']['HOST'],
    #                              user=settings.DATABASES['default']['USER'],
    #                              password=settings.DATABASES['default']['PASSWORD'],
    #                              db=settings.DATABASES['default']['NAME'],
    #                              charset='utf8mb4',
    #                              autocommit=autocommit,
    #                              cursorclass=pymysql.cursors.DictCursor,
    #                              local_infile=True)
    connection = sqlite3.connect("C:\Quantaco_Project\Quantaco\db.sqlite3")
    # cursor = connection.cursor()

    # # Example query: Create a table
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS test123 (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT NOT NULL,
    #     age INTEGER NOT NULL
    # )
    # ''')
    return connection