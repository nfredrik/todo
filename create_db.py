import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('todo.db')

# Optionally, create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create a table (optional)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL
)
''')

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database created successfully!")
