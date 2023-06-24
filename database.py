import sqlite3

# Set up database conncetion
connect = sqlite3.connect("users.db")
connect = sqlite3.connect("books.db")
connect.row_factory = sqlite3.Row   
# Create a cursor or pointer to the db
c = connect.cursor()

# Create the database table (books table)
# c.execute("""CREATE TABLE books(
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         subtitle TEXT,
#         authors TEXT,
#         image TEXT,
#         url TEXT
# )""")

# Create the database table (Users Table)
# c.execute("""CREATE TABLE users(
#         full_name text NOT NULL, 
#         user_email text,
#         password text,
#         confirm_password text,
#         PRIMARY KEY(user_email)
      
# )""")



connect.commit()
connect.close()


# Functions to Insert the users
def Add_User(full_name, email_id, password, confirm_password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?,?)", (full_name, email_id, password, confirm_password))
    conn.commit()
    conn.close()


# Function to query all users from database
def get_user():
    """A function to query user from database"""
    conn = sqlite3.connect(":memory:")
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row   
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall() 
    users = []
    for item in items:
        users.append(dict(item))
    return users


# Function to add book
def Add_book_data(id, title, subtitle, authors, image, url):
    conn = sqlite3.connect('books.db')
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES(?,?,?,?,?,?)", (id, title, subtitle, authors, image, url))
    conn.commit()
    conn.close()
