from database import DatabaseManager  # Assuming your class is in a file named database_manager.py

def main():
    database_name = '../db/database.db'
    connection = DatabaseManager.create_connection(database_name)
    
    # Create tables if they don't exist
    DatabaseManager.create_user_table(connection)
    DatabaseManager.create_vehicles_table(connection)

    # Accept user input and push data to the database

    name = ""
    email = ""

    DatabaseManager.push_user(connection, name, email)

    year = ""
    make = ""
    model = ""
    
    DatabaseManager.push_vehicle(connection, year, make, model)

    # Pull and print data from the database
    users = DatabaseManager.pull_user(connection)
    for user in users:
        print(user)

    vehicles = DatabaseManager.pull_vehicle(connection)
    for vehicle in vehicles:
        print(vehicle)

    connection.close()

if __name__ == "__main__":
    main()
