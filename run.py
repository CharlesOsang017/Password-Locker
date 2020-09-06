# !/usr/bin/env python3.8
from password import User

def create_password(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_password = User(fname,lname,phone,email)
    return new_password

def save_passwords(password):
    '''
    Function to save contact
    '''
    password.save_password()


def del_password(password):
    '''
    Function to delete a contact
    '''
    password.delete_password()

def find_password(number):
     '''
    Function that finds a contact by number and returns the contact
    '''
     return User.find_by_number(number)

def check_existing_passwords(number):
        '''
        Function that check if a contact exists with that number and return a Boolean
        '''
        return User.password_exist(number)

#
# def display_passwords():
#        return User.display_passwords()
#
# def main():
#     print("Hello Welcome to  Password-Locker. What is your name?")
#     password_name = input()
#
#     print(f"Hello {password_name}. Select what you would  like to do?")
#     print('\n')
#
#     while True:
#                     print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
#
#                     short_code = input().lower()
#
#                     if short_code == 'cc':
#                             print("New Contact")
#                             print("-"*10)
#
#                             print ("First name ....")
#                             f_name = input()
#
#                             print("Last name ...")
#                             l_name = input()
#
#                             print("Phone number ...")
#                             p_number = input()
#
#                             print("Email address ...")
#                             e_address = input()
#
#
#                             save_passwords(create_password(f_name,l_name,p_number,e_address)) # create and save new contact.
#                             print ('\n')
#                             print(f"New Contact {f_name} {l_name} created")
#                             print ('\n')
#
#                     elif short_code == 'dc':
#
#                             if display_passwords():
#                                     print("Here is a list of all your contacts")
#                                     print('\n')
#
#                                     for password in display_passwords():
#                                      print(f"Name: {password.first_name} {password.last_name}")
#                                      print(f"Phone number: {password.phone_number}")
#                                      print(f"Email address: {password.email}")
#
#
#
#                                     print('\n')
#                             else:
#                                     print('\n')
#                                     print("You dont seem to have any contacts saved yet")
#                                     print('\n')
#
#                     elif short_code == 'fc':
#
#                             print("Enter the number you want to search for")
#
#                             search_number = input()
#                             if check_existing_passwords(search_number):
#                                     search_password = find_password(search_number)
#                                     print(f"{search_password.first_name} {search_password.last_name}")
#                                     print('-' * 20)
#
#                                     print(f"Phone number.......{search_password.phone_number}")
#                                     print(f"Email address.......{search_password.email}")
#                             else:
#                                     print("That contact does not exist")
#
#                     elif short_code == "ex":
#                             print("Thank you for using Password-Locker..Good Bye .......")
#                             break
#                     else:
#                             print("I really didn't get that. Please use the short codes")
#
# if __name__ == '__main__':
#     main()
#
