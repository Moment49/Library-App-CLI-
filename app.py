class User:
    """A class to model the library app user"""
    def __init__(self, first_name, last_name, user_email, password, confirm_password):
        """Initialize the user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.password = password
        self.confirm_password = confirm_password
    def create_profile(self, **user_info):
        self.user_info = user_info
        self.user_info['first_name'] = self.first_name
        self.user_info['last_name'] = self.last_name
        self.user_info['user_email'] = self.user_email
        self.user_info['password'] = self.password
        self.user_info['confirm_password'] = self.confirm_password
        return user_info


def main():
    active = True
    while active:
        prompt = "\n......WELCOME TO BOOK STORE MANAGEMENT APPLICATION.....\n"
        prompt += "\n1 - Login as a User\n"
        prompt += "2 - Don't have an account? Create a User\n"
        prompt += "Please Select 1 or 2 to proceed: "
        user_response = input(prompt)
        if user_response == '1':
            print("\n...Login details...\n")
            message = ''
            while True:
                print("Enter email: ") 
                print("Enter password: ")
                message = input("enter: ")
                if message == 'no':
                    break 
            # active = False
        elif user_response == '2':
            print("\n...Create an account...\n")
            # while True:
            #     # get the details to create user account
            #     f_name = input("Enter first_name: ")
            #     l_name = input("Enter last_name: ")
            #     u_email = input("Enter email: ")
            #     u_password = input("Enter password: ")
            #     c_password = input("Enter confirm_password: ")
            #     if u_password != c_password:
            #         print("password does not match") 
            #         print("Try again")
            #     else:
            #         pass
                          
        else:
            print("Sorry, please select a valid option")






if __name__ == '__main__':
    main()








































# import requests
# import json


# # Making a Api get() request 
# url =  "https://www.dbooks.org/api/search/all"
# response = requests.get(url)
