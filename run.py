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

    while True:
        print(
            "*****  Welcome to password locker!!!  *****"
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
            print('\n')

            while confirm_password != created_user_password:
                print("-----------Invalid Password !-----------")
                print("-----------Enter user name-----------")
                created_user_password = input()
                print("-----------Confirm your password-----------")
                confirm_password = input()
                print('\n')
            else:
                print(
                    f"Hello {created_user_name}! You have successfully create your account! "
                    )
                print('\n')
                print("****** Proceed to login *******")
                print('\n')
                print("-----------Username-----------")
                entered_username = input()
                print("-----------Your password-----------")
                entered_password = input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print('\n')
                print("Invalid username or password")
                print("-----------Username-----------")
                entered_username = input()
                print("-----------Your password-----------")
                entered_password = input()
                print('\n')

            else:
                print('\n')
                print(f"******* Welcome {entered_username} to your account *******")
                print('\n')

                print("Select an option to continue: \n Enter 1, 2, 3, 4 or 5")
                print('\n')

            while True:
                print("1:view your saved credentials")
                print("2:Add new credentials")
                print("3:Remove  credentials")
                print("4:search new credentials")
                print("5:log out")
                option = input()

                if option == '2':
                    while True:
                        print("Do you wish to continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("-----------Enter account name-----------")
                            account_name = input()
                            print('\n')
                            print(
                                "** I can create a password for if you type in - 'rp' \n** Or create your own password with - 'cp'")
                            keyword = input().lower()

                            #Generates the random digit number
                            if keyword == 'rp':
                                account_password = random.randint(
                                    11111, 111111)
                                print('\n')
                                print('Automatically generated this for you')
                                print(f" ******* Account: {account_name}  *******")
                                print(f" ******* Password: {account_password}  *******")
                                print('\n')
                            elif keyword == 'cp':
                                print("Create your own password password")
                                account_password = input()
                                print(f" *******Account: {account_name} *******")
                                print(f" ******* Password: {account_password} *******")
                                print('\n')

                            else:
                                print(" ****** Enter a valid code *****")

                            # elif save_new_credential(create_new_credential(
                            #     account_name, account_password))

                        elif choice == 'cp':
                            break
                        else:
                            print("use 'y' for yes and 'n' for no")

                elif option == '1':
                    while True:
                        print("***** This is a list of your credentials *****")

                        if display_credential():

                            for credential in display_credential():
                                print(
                                    f"***** Account Name:{credential.account_name} *****")
                                print(
                                    f"***** Password:{credential.account_password}***** ")

                        else:

                            print('\n')
                            print("-------No credentials available------")
                            print('\n')

                        print("Back to menu? y/n")

                        back = input().lower()

                        back = input().lower()

                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("***** invalid option ******")
                            continue

                elif option == '5':
                    print(
                        "WARNING you will loose your details if you log out.Proceed? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("-------- You have logged out successfully --------")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("---- search for credential to delete ----")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(
                                f"Account Name: {search_credential.account_name}\n Password: {search_credential.account_password}")
                            print("Delete? y/n")

                            confirm = input().lower()
                            if confirm == 'y':
                                delete_credential(search_credential)
                                print("----- Account successfully removed -----")
                                break
                            elif confirm == 'n':
                                continue

                        else:
                            print("----- Account does not exist -----")
                            break
                
                elif option == '4':
                    while True:
                        print("continue? y/n")
                        choice = input().lower()
                        if choice == 'y':
                            print("--- Enter account name to find credentials ---")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account Name: {search_credential.account_name}\n Password: {search_credential.account_password}")
                            else:
                                print("---Sorry this account does not exist -----")
                        
                        elif choice == 'n':
                            break
                        else:
                            print("----- Invalid code -----")

                    print("----- Invalid code -----")
                    continue

        elif short_code == 'lg':
           print("----- welcome -----")
           print("----- Enter user name -----")
           default_user_name = input()

           print("----- Enter user name -----")
           default_user_name = input()
           print('\n')




if __name__ == '__main__':

    main()
