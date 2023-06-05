import emoji
import requests
import json


# User Class
class User:
    """A class to model the library app user"""
    def __init__(self, full_name, user_email, password, confirm_password):
        """Initialize the user attributes"""
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
    

# Book Class
class Book:
    """A call to model a book"""
    def __init__(self):
        pass


# List to hold user profile
users = []

#List to store all books from API 
books = []

#Make an API request to an end point to fetch books data
URL = "https://www.dbooks.org/api/search/all" 
response = requests.get(URL)
print(f"Status_code: {response.status_code}")

# Get access to the response data
data = response.text

# Parse or convert the json string to dictionary using the loads() method
res = json.loads(data)
for data in res['books']:
    print(data)
    # Append the book data to the books list
    books.append(data)

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
            print("Enter email: ") 
            print("Enter password: ")    
            # active = False
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
                    _user = User(f_name, u_email, u_password, c_password)
                    users.append(_user.create_profile())
                    print("\nCreating user...")
                    print("Login successful...")
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

                        # Get user input
                        user_action = input("Please select action to perform below: ")
                        if user_action == '1':
                            print()
                            for book in books:
                                print(book)
                            dashboard_active = False
        elif user_response == '3':
            # To terminate the main program
            active = False                
        else:
            print("Sorry, please select a valid option")


if __name__ == '__main__':
    main()










































# # Making a Api get() request 
# url =  "https://www.dbooks.org/api/search/all"
# response = requests.get(url)
