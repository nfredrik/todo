import sqlite3
DATABASE = 'nisse.db'

def create_user_table(conn) -> None:
    # Create User table
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def create_todo_table(conn) -> None:
# Create Todo table with foreign key linking to the User table
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                complete BOOLEAN DEFAULT FALSE,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
            )
        ''')

        conn.commit()   

def create_todo(conn, task='nuda', user_id=1):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Todo (task, user_id) VALUES (?, ?)', (task, user_id))
        conn.commit()

def create_user(conn, username='Johnny', password='hejhopp'):
    # Check if the username already exists
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM User WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print(f"Error: The username '{username}' is already taken.")
            return
        
        cursor.execute('INSERT INTO User (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print(f"User '{username}' created successfully.")             


def list_todos(conn,user_id=1):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Todo WHERE user_id = ?', (user_id,))
    todos = cursor.fetchall()
    return todos



# Function to connect to SQLite database using a context manager
def get_db_connection():

    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row  # Access rows like dictionaries
        cursor = conn.cursor()

        create_user_table(conn)

        create_todo_table(conn)

        create_user(conn)

        create_todo(conn)
        
        todos = list_todos(conn)
       
        for todo in todos:
            print(f"Task: {todo['task']}, Completed: {todo['complete']}")


        


    
get_db_connection()