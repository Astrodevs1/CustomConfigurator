import sqlite3

def create_connection(database_name='database.db'):
    
    connection = sqlite3.connect('../db/database.db')
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

    # Table schema output (debug)
    cursor.execute("PRAGMA table_info(users)")
    print(cursor.fetchall())

def insert_user(connection, name, email):
    """
    Insert a new user into 'users' table.

    Args:
    
    connection(sqlite3.Connection): Connection object.
    name (str): The name of the user.
    age (int): The age of the user.

    """

    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    connection.commit()

def get_users(connection):
    """
    Retrieve all users from the 'users' table.

    Args:
        connection (sqlite3.Connection): The database connection object.

    Returns:
        list: A list of tuples representing users.
    """
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def main():

    database_name = 'database.db'
    connection = create_connection(database_name)
    create_table(connection)

    insert_user(connection, 'John Doe', "EMAIL")
    insert_user(connection, 'Jane Smith', "EMAIL")

    # Retrieve and print all users
    users = get_users(connection)
    for user in users:
        print(user)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    main()