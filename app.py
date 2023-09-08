import emoji
import requests
import json
import qrcode
from database import Users, Books, session


# User Class For Input Record
class User:
    """A class to model the library app user"""
    def __init__(self, userid, full_name, user_email, password, confirm_password):
        """Initialize the user attributes"""
        self.userid = userid
        self.full_name = full_name
        self.user_email = user_email
        self.password = password
        self.confirm_password = confirm_password
    def create_profile(self, **user_info):
        self.user_info = user_info
        self.user_info['user_id'] = self.userid
        self.user_info['full_name'] = self.full_name
        self.user_info['user_email'] = self.user_email
        self.user_info['password'] = self.password
        self.user_info['confirm_password'] = self.confirm_password
        return user_info
    

# Book Class For Input Record
class Book:
    """A call to model a book"""
    def __init__(self, book_id, title, subtitle, authors, book_img, book_url):
        self.book_id = book_id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.book_img = book_img
        self.book_url = book_url
    def Add_book(self, **book_details):
        self.book_details = book_details
        self.book_details['id'] = self.book_id
        self.book_details['title'] = self.title
        self.book_details['subtitle'] = self.subtitle
        self.book_details['authors'] = self.authors
        self.book_details['image'] = self.book_img
        self.book_details['url'] = self.book_url
        return book_details
    
#List to store all books from API and from the book class
books_list = []

#Make an API request to an end point to fetch books data
# URL = "https://www.dbooks.org/api/search/all" 
# response = requests.get(URL)
# print(f"Status_code: {response.status_code}")

# # Get access to the response data
# data = response.text

# # Parse or convert the json string to dictionary using the loads() method
# res = json.loads(data)
# for data in res['books']:
#     # Append the book data to the books list
#     books_list.append(data)

# print(books_list)
# Get the data from db
result = session.query(Users).all()
print(result)


# List to hold user profile
users_list = []

# Main Program
def main():
    """This is the main program function"""
    active = True
    while active:
        em_book = emoji.emojize("📚")
        em_login = emoji.emojize("🙂")
        em_new = emoji.emojize("😞")
        main_prompt = f"\n...WELCOME TO BOOK STORE MANAGEMENT APPLICATION...{em_book}{em_book}{em_book}\n"
        main_prompt += f"\n1 - Login as a User {em_login}\n"
        main_prompt += f"2 - Don't have an account{em_new} ? Create a User\n"
        main_prompt += f"3 - Exit the application \n"
        main_prompt += "Please select 1, 2 or 3 to proceed: "
        user_response = input(main_prompt)

        # Login Into Account
        if user_response == '1':
            print("\n...Login details...\n")
            log_active = True
            while log_active:
                #Get user email and password
                user_id = input("Enter User_id: ")
                user_password = input("Enter password: ")
                user = session.query(Users).filter(Users.userId==user_id, Users.password==user_password).first()

                if user is not None:
                    # Stop the main and login_active loop once email and password verified
                    # active = False 
                    log_active = False
                    dashboard_active = True
                    while dashboard_active:
                        print('found user!!! Login successful')
                        em_show = emoji.emojize("📚")
                        em_add = emoji.emojize("📖")
                        em_update = emoji.emojize("📗")
                        em_delete = emoji.emojize("📕")
                        print(f"\n...Welcome Back - {user.full_name}\n")
                        print(f"1 - Show all books {em_show}{em_show} ")
                        print(f"2 - Add a book{em_add}")
                        print(f"3 - Update a book{em_update}")
                        print(f"4 - Delete a book{em_delete}")
                        print("5  - Search for a book")
                        print("6 - Generate book QR-CODE")
                        print("7 - Logout")

                        # Get user input
                        user_action = input("Please select action to perform below: ")
                        if user_action == '1':
                            book_details =  session.query(Books).filter(Books.book_user_id==user_id).first() 
                            if book_details is None:
                                print('<<<No books to show>>>')     
                                dashboard_active = False
                                active = False
                            else:
                                for book in book_details:
                                    print("\n<<<Show all books>>>\n")
                                    print(f"'Book ISBN': {book.book_id}\n 'Book Title': {book.title}\n \'Book Subtitle': {book.subtitle}\n \
                                        'Book Authors': {book.authors}\n 'Book Image': {book.image}\n 'Book URL': {book.url}")
                                dashboard_active = False
                        if user_action == '2':
                            print("<<<ADD BOOK>>>")
                            book_no = int(input("ISBN: "))
                            book_title = input("Book title: ")
                            book_subtitle = input("Book subtitle: ")
                            book_authors = input("Book authors: ")
                            book_image = input("Book image_url: ")
                            book_url = input("Book url: ")
                            # Create a book Object
                            book = Book(book_no, book_title, book_subtitle, book_authors, book_image, book_url)
                            
                            # Add book  Object to books_list
                            books_list.append(book.Add_book())

                            # Push book data to db
                            book = Books(book_id=book_no, title=book_title, subtitle=book_subtitle, 
                                            authors=book_authors, image=book_image, url=book_url, book_creator=user)
                            session.add(book)
                            session.commit()
                            print("Book Added")
                            dashboard_active = False 
                            active = False

                        if user_action == '3':
                            print("<<<UPDATE BOOK>>>")
                            user = session.query(Users).filter(Users.userId == user_id).first()
                            user_books = user.books
                            print(">>>List of All books<<<")
                            for user_book in user_books:
                                print(f"ISBN: {user_book.book_id}\nTitle:{user_book.title}\nAuthors: {user_book.authors}\nBook_URL: {user_book.url}\n")
                            
                            # Update the book based on the Isbn selected
                            print("Please Enter an ISBN to update")
                            isbn_ = input("ISBN: ")
                            book_update = session.query(Books).filter(Books.book_id==isbn_).first()
                            if book_update is not None:
                                isbn_update = input("Enter new ISBN: ")
                                title_update = input("Book title: ")
                                subtitle_update = input("Book subtitle: ")
                                authors_update = input("Book authors: ")
                                image_update = input("Book image_url: ")
                                url_update = input("Book url: ")

                                # Update the book details
                                x = session.query(Books).get(isbn_)
                                x.book_id = isbn_update
                                x.title = title_update
                                x.subtitle = subtitle_update
                                x.authors = authors_update
                                x.image = image_update
                                x.url = url_update
                                # Commit your changes
                                session.commit()
                                print("Book updated...")
                                dashboard_active = False 
                            else:
                                print("Invalid Isbn or Book does not exist")
                                dashboard_active = False 
                        if user_action == '4':
                            print("<<<DELETE BOOK>>>")
                            user = session.query(Users).filter(Users.userId == user_id).first()
                            user_books = user.books
                            print(">>>List of All books<<<")
                            for user_book in user_books:
                                print(f"ISBN: {user_book.book_id}\nTitle:{user_book.title}\nAuthors: {user_book.authors}\nBook_URL: {user_book.url}\n")

                             # Delete a book based on the Isbn selected
                            print("Please Enter an book Isbn to delete")
                            isbn_ = input("ISBN: ")
                            book_delete = session.query(Books).get(isbn_)
                            session.delete(book_delete)
                            session.commit()
                            print("Book deleted...")
                            dashboard_active = False 

                        if user_action == '5':
                            search_active = True
                            while search_active:        
                                print("<<<Search for book>>>")
                                print("Please select a search term")
                                print(f"1 - Search by Authors ")
                                print(f"2 - Search by Title ")
                                print(f"3 - Search by Subtitle ")
                                print(f"4 - Search by Isbn number ")

                                user_select = input("Please select an action to perform: ")
                                if user_select == '1':
                                    print("search by Authors")
                                    search_author = input("Search authors...: ")
                                    search_results = session.query(Books).filter(Books.authors.like(f"%{search_author}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '2':
                                    print("search by Title")
                                    search_title = input("Search title...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '3':
                                    print("search by Subtitle")
                                    search_title = input("Search Subtitle...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '4':
                                    print("Search by Isbn number")
                                    search_title = input("Search Isbn...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                dashboard_active = False 
                                search_active = False
                        if user_action == '6':
                            print("<<<Generate Book QR-Code>>>")
                            user_details = session.query(Users).filter(Users.userId == user_id).first()
                            print("List of books Url")
                            for book in  user_details.books:
                                print(f"Book_link: {book.url}")
                            qr = qrcode.QRCode(
                                        version=1,
                                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                                        box_size=10,
                                        border=4)
                            
                            book_url_qr = input("Enter book url to generate QRcode: ")
                            qr.add_data(book_url_qr)
                            qr.make(fit=True)
                            img = qr.make_image(fill_color="black", back_color="white")
                            img.save('book1.png')
                            dashboard_active = False
                        if user_action == '7':
                            print("Logging out..")
                            print("Please Login...")
                            dashboard_active = False 
                            log_active = True
                else:
                    print("Invalid user_id or password")
        #Create an account 
        elif user_response == '2':
            user_isValid = True
            while user_isValid:
                em = emoji.emojize("↩")
                prompt = "\nEnter '1' to proceed to user registration...\n"
                prompt += f"Enter 'return' to go back to Main page {em} : "
                user_select = input(prompt)
                if user_select == 'return':
                    # Display the main page if user selects return
                    user_response = input(main_prompt)    
                else:
                    print("\n##..Create account..##\n")
                    # get the details to create user account
                    userid = input("Enter userid: ")
                    f_name = input("Enter full_name: ")
                    u_email = input("Enter email: ")
                    u_password = input("Enter password: ")
                    c_password = input("Enter confirm_password: ")

                    # Check for password validation
                    while u_password != c_password: 
                        # Prompt the user to enter password again
                        print("password does not match")
                        u_password = input("Enter password: ")
                        c_password = input("Enter confirm_password: ")
                        if u_password != c_password:
                            print("password does not match")
                    # Creates the user after registering & Appends user to the list
                    _user = User(userid, f_name, u_email, u_password, c_password)
                    users_list.append(_user.create_profile())

                    # Push user records to database
                    user = Users(userId=userid, full_name=f_name, user_email=u_email, password=u_password, confirm_password = c_password)
                    session.add(user)
                    session.commit()
                    print("Sign up successful...")
                    user_isValid = False 
                    active = False
                    dashboard_active = True
                    while dashboard_active:
                        em_show = emoji.emojize("📚")
                        em_add = emoji.emojize("📖")
                        em_update = emoji.emojize("📗")
                        em_delete = emoji.emojize("📕")
                        print(f"\n...Welcome to Dashboard - {f_name}\n")
                        print(f"1 - Show all books {em_show}{em_show} ")
                        print(f"2 - Add a book{em_add}")
                        print(f"3 - Update a book{em_update}")
                        print(f"4 - Delete a book{em_delete}")
                        print("5 - Search for a book")
                        print("6 - Generate book QR-CODE")
                        print("7 - Logout")
                        # Get user input
                        user_action = input("Please select action to perform below: ")
                        if user_action == '1':
                            # Will write a logic to check if there are any books if not write books empty
                            book_details =  session.query(Books).filter(Books.book_user_id==userid) .first()
                            if book_details is None:
                                print('<<<No books to show>>>')     
                                dashboard_active = False
                                active = False
                            if book_details is not None:
                                for book in book_details:
                                    print("\n<<<Show all books>>>\n")
                                    print(f"'Book ISBN': {book.book_id}\n 'Book Title': {book.title}\n \'Book Subtitle': {book.subtitle}\n \
                                        'Book Authors': {book.authors}\n 'Book Image': {book.image}\n 'Book URL': {book.url}")
                                dashboard_active = False
                        if user_action == '2':
                            print("<<<ADD BOOK>>>")
                            book_no = int(input("ISBN: "))
                            book_title = input("Book title: ")
                            book_subtitle = input("Book subtitle: ")
                            book_authors = input("Book authors: ")
                            book_image = input("Book image_url: ")
                            book_url = input("Book url: ")
                            # Create a book Object
                            book = Book(book_no, book_title, book_subtitle, book_authors, book_image, book_url)
                            
                            # Add book  Object to books_list
                            books_list.append(book.Add_book())

                            # Push book data to db
                            book = Books(book_id=book_no, title=book_title, subtitle=book_subtitle, 
                                            authors=book_authors, image=book_image, url=book_url, book_creator=user)
                            session.add(book)
                            session.commit()
                            print("Book Added")
                            dashboard_active = False 
                            active = False
 
                            dashboard_active = False 
                        if user_action == '3':
                            print("<<<UPDATE BOOK>>>")
                            user = session.query(Users).filter(Users.userId == userid).first()
                            user_books = user.books
                            print(">>>List of All books<<<")
                            for user_book in user_books:
                                print(f"ISBN: {user_book.book_id}\nTitle:{user_book.title}\nAuthors: {user_book.authors}\nBook_URL: {user_book.url}\n")
                            
                            # Update the book based on the Isbn selected
                            print("Please Enter an ISBN to update")
                            isbn_ = input("ISBN: ")
                            book_update = session.query(Books).filter(Books.book_id==isbn_).first()
                            if book_update is not None:
                                isbn_update = input("Enter new ISBN: ")
                                title_update = input("Book title: ")
                                subtitle_update = input("Book subtitle: ")
                                authors_update = input("Book authors: ")
                                image_update = input("Book image_url: ")
                                url_update = input("Book url: ")

                                # Update the book details
                                x = session.query(Books).get(isbn_)
                                x.book_id = isbn_update
                                x.title = title_update
                                x.subtitle = subtitle_update
                                x.authors = authors_update
                                x.image = image_update
                                x.url = url_update
                                # Commit your changes
                                session.commit()
                                print("Book updated...")
                                dashboard_active = False 
                            else:
                                print("Invalid Isbn or Book does not exist")
                                dashboard_active = False 
                            dashboard_active = False 
                        if user_action == '4':
                            print("<<<DELETE BOOK>>>")
                            user = session.query(Users).filter(Users.userId == user_id).first()
                            user_books = user.books
                            print(">>>List of All books<<<")
                            for user_book in user_books:
                                print(f"ISBN: {user_book.book_id}\nTitle:{user_book.title}\nAuthors: {user_book.authors}\nBook_URL: {user_book.url}\n")

                             # Delete a book based on the Isbn selected
                            print("Please Enter an book Isbn to delete")
                            isbn_ = input("ISBN: ")
                            book_delete = session.query(Books).get(isbn_)
                            session.delete(book_delete)
                            session.commit()
                            print("Book deleted...")
                            dashboard_active = False 
                        if user_action == '5':
                            search_active = True
                            while search_active:        
                                print("<<<Search for book>>>")
                                print("Please select a search term")
                                print(f"1 - Search by Authors ")
                                print(f"2 - Search by Title ")
                                print(f"3 - Search by Subtitle ")
                                print(f"4 - Search by Isbn number ")

                                user_select = input("Please select an action to perform: ")
                                if user_select == '1':
                                    print("search by Authors")
                                    search_author = input("Search authors...: ")
                                    search_results = session.query(Books).filter(Books.authors.like(f"%{search_author}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '2':
                                    print("search by Title")
                                    search_title = input("Search title...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '3':
                                    print("search by Subtitle")
                                    search_title = input("Search Subtitle...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                elif user_select == '4':
                                    print("Search by Isbn number")
                                    search_title = input("Search Isbn...: ")
                                    search_results = session.query(Books).filter(Books.title.like(f"%{search_title}"))
                                    for row in search_results:
                                        print(f"ISBN: {row.book_id}\n Title: {row.title}\n Subtitle: {row.subtitle}\n Authors: {row.authors}\n Image: {row.image}\n Url: {row.url}")
                                dashboard_active = False 
                                search_active = False
                        if user_action == '6':
                            print("Generate QR-Code")
                        if user_action == '7':
                            print("Logging out..")
                            print("Please Login...")
                            dashboard_active = False 
                            log_active = True 

        # Exit Program
        elif user_response == '3':
            # To terminate the main program
            active = False                
        else:
            print("Sorry, please select a valid option")


if __name__ == '__main__':
    main()



# # # Making a Api get() request 
# # url =  "https://www.dbooks.org/api/search/all"
# # response = requests.get(url)