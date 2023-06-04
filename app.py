class User:
    def __init__(self, first_name, last_name, user_email, password, confirm_password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.password = password
        self.confirm_password = confirm_password
    def user_profile(self, **user_info):
        self.user_info = user_info
        self.user_info['first_name'] = self.first_name
        self.user_info['last_name'] = self.last_name
        self.user_email['user_email'] = self.user_email
        self.password['password'] = self.password
        self.confirm_password['confirm_password'] = self.confirm_password


def main():
    active = True
    while active:
        prompt = "\n......WELCOME TO BOOK STORE MANAGEMENT APPLICATION.....\n"
        prompt += "\n1 - Login as a User\n"
        prompt += "2 - Don't have an account? Create User\n"
        prompt += "Please Select 1 or 2 to proceed: "
        user_response = input(prompt)
        if user_response == '1':
            print("\n...Login details...\n")
            print("Enter email: ") 
            print("Enter password: ")
            active = False
        elif user_response == '2':
            print("\n...Create an account...\n")
            print("Enter first_name: ")
            print("Enter last_name: ")
            print("Enter email: ")
            print("Enter password: ")
            print("Enter Confirm password: ")
            active = False
        else:
            print("Sorry, please select a valid option")






if __name__ == '__main__':
    main()








































# import requests
# import json


# # Making a Api get() request 
# url =  "https://www.dbooks.org/api/search/all"
# response = requests.get(url)
