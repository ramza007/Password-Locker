#!/usr/bin/env python
import random
from user import User
from credentials import Credentials

# functions to add credentials


def create_new_credential(account_name, account_password):
    '''
    method that creates  new  account name
    '''
    new_credential = Credentials(account_name, account_password)

    return new_credential


def save_new_credential(credentials):
    '''
    method to save new credentials
    '''

    credentials.save_credentials()


def find_credential(account_name):
    '''
    method to find a credential that has been created
    '''

    return Credentials.find_by_name(account_name)


def display_credential():
    '''
    method to dispay a credential that has been created
    '''
    return Credentials.display_credentials()


def delete_credential(credentials):
    '''
    method to delete a credential that has been created
    '''

    return Credentials.delete_credentials(credentials)


def main():
    users = {}  # Dictionary to store user credentials

    print('\n')
    while True:
        print(
            "********************  Welcome to password locker!!! ********************"
        )
        print('\n')
        print("""Use these short codes to navigate: \n "nu"- add new user \n "lg"-login to your created account \n "ex"-to exit the system""")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('-----------create username---------')
            created_user_name = input()

            print('-----------create password---------')
            created_user_password = input()

            print('-----------confirm password---------')
            confirm_password = input()

            if created_user_password == confirm_password:
                users[created_user_name] = created_user_password
                print(f"User {created_user_name} created successfully!")
            else:
                print("Passwords do not match. Please try again.")
            
            print('Do you want to create another user? (yes/no)')
            create_another = input().lower()
            if create_another == 'no':
                continue  # This will take you back to the main menu

        elif short_code == 'lg':
            print('-----------enter username---------')
            username = input()

            print('-----------enter password---------')
            password = input()

            if username in users and users[username] == password:
                print(f"Welcome {username}!")
                # Add further logic for logged-in users here
            else:
                print("Invalid username or password. Please try again.")

        elif short_code == 'ex':
            print("Exiting the system...")
            break

        else:
            print("Invalid short code. Please try again.")

if __name__ == '__main__':
    main()
