#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, db_name, state_name = sys.argv[1:]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query to get cities of the specified state
    try:
        cursor.execute(
            "SELECT cities.name FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id",
            (state_name,)
        )
    except MySQLdb.Error as e:
        print("Error executing the query:", e)
        cursor.close()
        db.close()
        sys.exit(1)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the results
    if cities:
        city_names = ", ".join(city[0] for city in cities)
        print(city_names)
    else:
        print("No cities found for the specified state.")

    # Close the cursor and database connection
    cursor.close()
    db.close()
