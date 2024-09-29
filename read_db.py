import sqlite3

# Function to connect to the SQLite database and fetch data
def read_from_database(db_file, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Create a SQL query to select all data from the table
        query = f"SELECT * FROM {table_name};"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Check if there are any rows
        if rows:
            print(f"Data from {table_name}:")
            for row in rows:
                print(row)
        else:
            print(f"No data found in table {table_name}.")

    except sqlite3.Error as e:
        print(f"Error reading from database: {e}")

    finally:
        # Close the connection
        if conn:
            conn.close()

# Main script
if __name__ == "__main__":
    # Specify the SQLite database file
    db_file = "todo.db"

    # Specify the table name to read from
    table_name = "tasks"

    # Call the function to read data from the specified table
    read_from_database(db_file, table_name)
