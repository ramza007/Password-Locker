#!/usr/bin/env python
import random
from user import User
from credentials import Credentials

# functions to add our credentials


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

    while True:
        print("Welcome to password locker!!!")
        print('\n')
        print("Use these short codes to navigate - new user use 'nu' - login to your account, 'lg' - 'ex' to exit the system")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Invalid ! Password oes not match!")
                print("Try again")
                created_user_password = input()
                print("Confirm your password")
                confirm_password = input()














                
if __name__ == '__main__':

    main()
