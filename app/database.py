import sqlite3

def create_connection(database_name='database.db'):
    
    connection = sqlite3.connect('db/database.db')
    return connection



def create_table(connection):
    """
    Create 'users' table.
    
    Args:

    connection(sqlite3.Connection): Connection object.
    name (str): Username.
    email (str): E-mail address.
    
    """
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')
    connection.commit()