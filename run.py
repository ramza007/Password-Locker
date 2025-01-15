#!/usr/bin/env python
import random
import string
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


def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


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
                print(f"\nWelcome {username}!")
                while True:
                    print("""Use these short codes to navigate: \n "cc"- create credential \n "dc"- display credentials \n "lo"- logout""")
                    user_short_code = input().lower()
                    if user_short_code == 'cc':
                        print('-----------enter account name---------')
                        account_name = input()
                        print('Do you want to create your own password or generate one? (c/g)')
                        password_option = input().lower()
                        if password_option == 'c':
                            print('-----------enter account password---------')
                            account_password = input()
                        elif password_option == 'g':
                            account_password = generate_password()
                            print("----------")
                            print(f"Generated password: {account_password}")
                            print("----------")
                        else:
                            print("Invalid option. Please try again.")
                            continue
                        new_credential = Credentials(account_name, account_password)
                        new_credential.save_credentials()
                        print(f"Credential for {account_name} created successfully!")
                    elif user_short_code == 'dc':
                        credentials = Credentials.display_credentials()
                        if credentials:
                            for credential in credentials:
                                print("----------")
                                print(f"Account: {credential.account_name}, Password: {credential.account_password}")
                                print("----------")
                        else:
                            print("\n----------No credentials found.----------\n")
                    elif user_short_code == 'lo':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid short code. Please try again.")
            else:
                print("Invalid username or password. Please try again.")

        elif short_code == 'ex':
            print("Exiting the system...")
            break

        else:
            print("Invalid short code. Please try again.")

if __name__ == '__main__':
    main()
