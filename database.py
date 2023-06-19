import sqlite3

# Set up database conncetion
connect = sqlite3.connect("users.db")

# Create a cursor or pointer to the db
c = connect.cursor()

# Create the database table (books table)
# c.execute("""CREATE TABLE books(
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         subtitle TEXT,
#         authors TEXT,
#         image TEXT,
#         url TEXT,
#         email_id TEXT,
#         FOREIGN KEY(email_id) REFERENCES users(email_id) ON DELETE SET NULL
# )""")

# Create the database table (Users Table)
# c.execute("""CREATE TABLE users(
#         full_name text NOT NULL, 
#         user_email text,
#         password text,
#         confirm_password text,
#         PRIMARY KEY(user_email)
      
# )""")


# Functions to Insert the users
def Add_User(full_name, email_id, password, confirm_password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?,?)", (full_name, email_id, password, confirm_password))
    conn.commit()
    conn.close()

# c.execute("SELECT * FROM users")

# Function to query all users from database
def get_user():
    """A function to query user from database"""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    return items
    

get_user()










# Save db changes
connect.commit()

# Close db connection
connect.close()