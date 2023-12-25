import sqlite3

class DatabaseManager:

    @staticmethod
    def create_connection(database_name='database.db'):
        connection = sqlite3.connect(database_name)
        return connection

    @staticmethod
    def create_table(connection):
        """
        Create 'users' table.

        Args:
            connection (sqlite3.Connection): Connection object.
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

    @staticmethod
    def insert_user(connection, name, email):
        """
        Insert a new user into 'users' table.

        Args:
            connection (sqlite3.Connection): Connection object.
            name (str): The name of the user.
            email (str): The email address of the user.
        """
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        connection.commit()

    @staticmethod
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

    @staticmethod
    def main():
        database_name = 'database.db'
        connection = DatabaseManager.create_connection(database_name)
        DatabaseManager.create_table(connection)

        DatabaseManager.insert_user(connection, 'John Doe', 'john@example.com')
        DatabaseManager.insert_user(connection, 'Jane Smith', 'jane@example.com')

        # Retrieve and print all users
        users = DatabaseManager.get_users(connection)
        for user in users:
            print(user)

        # Close the connection
        connection.close()

if __name__ == "__main__":
    DatabaseManager.main()