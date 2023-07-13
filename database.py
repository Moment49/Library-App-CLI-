# Database Using an ORM-SQLALCHEMY
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



base = declarative_base()

# Define the db class model
class Users(base):
    __tablename__ = "users"
    userid = Column("userId", String, primary_key=True)
    full_name = Column("full_name", String, nullable=False)
    user_email = Column("user_email", String)
    password = Column("password", String)
    confirm_password = Column("confirm_password", String) 

    def __init__(self, userid, full_name, user_email, password, confirm_password):
        self.userid = userid
        self.full_name = full_name
        self.user_email = user_email
        self.password = password
        self.confirm_password = confirm_password
    
    def __repr__(self):
        return f"({self.full_name}),{self.user_email}, {self.password}, {self.confirm_password}"


# Book MODEL
class Books(base):
    __tablename__ = 'books'
    book_id = Column("book_id", Integer, primary_key=True)
    title = Column('title', String)
    subtitle = Column('subtitle', String)
    authors = Column('authors', String)
    image = Column('image', String)
    url = Column('url', String)
    book_user = Column(String, ForeignKey(Users.userid))

    def __init__(self, book_id, title, subtitle, authors, image, url, book_user):
        self.book_id = book_id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.image = image
        self.url = url 
        self.book_user = book_user

    def __repr__(self):
        return f"{self.book.id} {self.title}{self.authors} {self.book_user}"
    



engine = create_engine("sqlite:///users.db", echo=True)
base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)




# import sqlite3

# Set up database conncetion
# connect = sqlite3.connect("users.db")
# connect = sqlite3.connect("books.db")
# connect.row_factory = sqlite3.Row   

# # Create a cursor or pointer to the db
# c = connect.cursor()
# c.execute("PRAGMA foreign_keys = ON")

# # Create the database table (books table)
# c.execute("""CREATE TABLE books(
#         id INTEGER PRIMARY KEY,
#         title TEXT,
#         subtitle TEXT,
#         authors TEXT,
#         image TEXT,
#         url TEXT
          
# )""")

# # Create the database table (Users Table)
# c.execute("""CREATE TABLE users(
#         userID Integer PRIMARY KEY 
#         full_name text NOT NULL, 
#         user_email text,
#         password text,
#         confirm_password text,
      
# )""")


# connect.commit()
# connect.close()

# # Functions to Insert the users
# # def Add_User(full_name, email_id, password, confirm_password):
# #     conn = sqlite3.connect('users.db')
# #     c = conn.cursor()
# #     c.execute("INSERT INTO users VALUES(?,?,?,?)", (full_name, email_id, password, confirm_password))
# #     conn.commit()
# #     conn.close()


# # # Function to query all users from database
# # def get_user():
# #     """A function to query user from database"""
# #     # conn = sqlite3.connect(":memory:")
# #     conn = sqlite3.connect('users.db')
# #     conn.row_factory = sqlite3.Row   
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM users")
# #     items = c.fetchall() 
# #     users = []
# #     for item in items:
# #         users.append(dict(item))
# #     return users


# # # Function to add book
# # def Add_book_data(id, title, subtitle, authors, image, url):
# #     conn = sqlite3.connect('books.db')
# #     # conn = sqlite3.connect(":memory:")
# #     conn.row_factory = sqlite3.Row
# #     c = conn.cursor()
# #     c.execute("INSERT INTO books VALUES(?,?,?,?,?,?)", (id, title, subtitle, authors, image, url))
# #     conn.commit()
# #     conn.close()


# # # Show All Books
# # def show_books():
# #     conn = sqlite3.connect('books.db')
# #     conn.row_factory = sqlite3.Row
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM books")
# #     items = c.fetchall()
# #     books = []
# #     for item in items:
# #         books.append(dict(item))
# #     return books

# # Show user books

