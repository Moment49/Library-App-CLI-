import sqlite3

# Set up database conncetion
connect = sqlite3.connect("users.db")

# Create a cursor or pointer to the db
c = connect.cursor()

# Create the database table (Users Table)















# Save db changes
connect.commit()

# Close db connection
connect.close()