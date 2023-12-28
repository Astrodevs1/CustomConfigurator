import sqlite3

class DatabaseManager:

    @staticmethod
    def create_connection(database_name='database.db'):
        connection = sqlite3.connect(database_name)
        return connection

    @staticmethod
    def create_user_table(connection):
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
    def create_vehicles_table(connection):

        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vehicles (
                id INTEGER PRIMARY KEY,
                year INTEGER,
                make TEXT,
                model TEXT,
            )  
                       
        ''')
        connection.commit()

        # Table schema output (debug)
        cursor.execute("PRAGMA table_info(vehicles)")
        print(cursor.fetchall())

    @staticmethod
    def push_vehicle(connection, year, make, model):
        
        year = input("Enter Model Year: ")
        make = input("Enter Vehicle Make: ")
        model = input("Enter vehicle Model: ")

        cursor = connection.cursor()
        cursor.execute('INSERT INTO vehicles (year, make, model) VALUES (?, ?, ?)', (year, make, model))
        connection.commit()  

    @staticmethod
    def pull_vehicle(connection, year, make, model):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM vehicles')
        return cursor.fetchall()

    @staticmethod
    def push_user(connection, name, email):

        name = input("Enter Username: ")
        email = input("Enter Email: ")

        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        connection.commit()

    @staticmethod
    def pull_user(connection):
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    @staticmethod
    def main():
        database_name = 'database.db'
        connection = DatabaseManager.create_connection(database_name)
        DatabaseManager.create_user_table(connection)
        DatabaseManager.create_vehicles_table(connection)

        users = DatabaseManager.pull_user(connection)
        for user in users:
            print(user)
        
        vehicles = DatabaseManager.pull_vehicle(connection)
        for vehicle in vehicles:
            print(vehicle)
            
        connection.close()

if __name__ == "__main__":
    DatabaseManager.main()