# Database Using an ORM-SQLALCHEMY
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# Base class Obj
Base = declarative_base()

# Users Model
class Users(Base):
    __tablename__ = "users"
    userId = Column("userId", String, primary_key=True)
    full_name = Column("full_name", String, nullable=False)
    user_email = Column("user_email", String)
    password = Column("password", String)
    confirm_password = Column("confirm_password", String) 
    books = relationship('Books', backref='book_creator', cascade="all, delete")
    
    def __repr__(self):
        return f"userId:{self.userId} full_name:{self.full_name} user_email:{self.user_email} password:{self.password} confirm_password:{self.confirm_password} "

# Book MODEL
class Books(Base):
    __tablename__ = 'books'
    book_id = Column("book_id", Integer, primary_key=True)
    title = Column('title', String)
    subtitle = Column('subtitle', String)
    authors = Column('authors', String)
    image = Column('image', String)
    url = Column('url', String)
    book_user_id = Column(String, ForeignKey('users.userId'))

    def __repr__(self):
        return f"{self.book_id} {self.title} {self.subtitle} {self.image} {self.url} {self.authors} {self.book_user_id}"
    

# Create the db engine and instantiate a connection
engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
# Create session obj to handle db operations
Session = sessionmaker(bind=engine)
session = Session()




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

