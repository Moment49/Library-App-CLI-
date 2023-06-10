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
#         email_id text,
#         password text,
#         confirm_password text,
#         PRIMARY KEY(email_id)
      
# )""")

# Functions to Insert the users
def Add_User(full_name, email_id, password, confirm_password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?,?)", (full_name, email_id, password, confirm_password))
    conn.commit()
    conn.close()

c.execute("SELECT * FROM users")












# Save db changes
connect.commit()

# Close db connection
connect.close()