import emoji
import requests
import json
import database


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
    


# List to hold user profile
users_list = [{'full_name':'Ibenacho Elvis', 'user_email':'elv@gmail.com', 'password': 'elv123', 'confirm_password':'elv123'}]

# database.Users()

# Call the user_info from db
# users = database.get_user()
# # Iterate over the info from db and push user back to the list
# for user in users:
#     users_list.append(user)
# print(users_list)


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
        if user_response == '1':
            print("\n...Login details...\n")
            log_active = True
            while log_active:
                #Get user email and password
                user_email = input("Enter email: ")
                user_password = input("Enter password: ")
                for user in users_list:
                    # Check if users has already created account
                    if user_email in user.values() and user_password in user.values():
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
                            print(f"\n...Welcome Back - {user['full_name']}\n")
                            print(f"1 - Show all books {em_show}{em_show} ")
                            print(f"2 - Add a book{em_add}")
                            print(f"3 - Update a book{em_update}")
                            print(f"4 - Delete a book{em_delete}")
                            print("5 - Search for a book")
                            print("6 - Logout")

                            # Get user input
                            user_action = input("Please select action to perform below: ")
                            if user_action == '1':
                                print("Displaying All user added books...")
                                session = database.Session()
                                result =  session.query(database.Books()).all()
                                for row in result:
                                    print(row.book_id,  row.title, row.subtitle, row.authors, row.image, row.url)
                                # for book in books_list:
                                #     print(book)
                                # books = database.show_books()
                                # for book in books:
                                #     print(book)
                                dashboard_active = False
                                active = False 
                            if user_action == '2':
                                print("Adding book..")
                                book_no = int(input("ISBN: "))
                                book_title = input("Book title: ")
                                book_subtitle = input("Book subtitle: ")
                                book_authors = input("Book authors: ")
                                book_image = input("Book image_url: ")
                                book_url = input("Book url: ")
                                book = Book(book_no, book_title, book_subtitle, book_authors, book_image, book_url)
                                
                                # Add book to books_list
                                books_list.append(book.Add_book())
                                # Push book data to db
                                session = database.Session()
                                # user_id_check = session.query(database.Users()).filter(database.Users().email == user_email)
                                # print(user_id_check)
                                book1 = database.Books(book_no, book_title, book_subtitle, book_authors, book_image, book_url,book_user=12345)
                                session.add(book1)
                                session.commit()
                                dashboard_active = False 
                            if user_action == '3':
                                print("###Update book###..")
                                print("Enter book no(ISBN)")
                                books = database.show_books()
                                for book in books:
                                    print(book)
                                book_no = input("Please Enter Book number: ")
                                
                                dashboard_active = False 
                            if user_action == '4':
                                print("Delete book..")
                                dashboard_active = False 
                            if user_action == '5':
                                print("Adding book..")
                                dashboard_active = False 
                            if user_action == '6':
                                print("Logging out..")
                                dashboard_active = False 
                                active = True

                    elif user_email not in user.values() and user_password not in user.values():
                        print('User not found!! Please create account')
                    else:
                        print("Invalid email or password")
                
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
                    
                    # Creates the user after registering
                    _user = User(userid, f_name, u_email, u_password, c_password)
                    # Appends user to the list
                    users_list.append(_user.create_profile())

                    # Push users to the database(users)
                    # database.Add_User(f_name, u_email, u_password, c_password)
                    user = database.Users(userid, f_name, u_email, u_password, c_password)
                    session = database.Session()
                    session.add(user)
                    session.commit()
                    print("\nCreating user...")
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
                        print("6 - Logout")
                        # Get user input
                        user_action = input("Please select action to perform below: ")
                        if user_action == '1':
                            for book in books_list:
                                print(book)
                            dashboard_active = False
                        if user_action == '2':
                            print("Adding book..")
                            dashboard_active = False 
                        if user_action == '3':
                            print("Update book..")
                            dashboard_active = False 
                        if user_action == '4':
                            print("Delete book..")
                            dashboard_active = False 
                        if user_action == '5':
                            print("Adding book..")
                            dashboard_active = False 
                        if user_action == '6':
                            print("Logging out..")
                            dashboard_active = False 

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
