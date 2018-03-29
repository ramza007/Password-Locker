import random
from user import User
from credentials import Credentials

# functions to add our credentials


def create_new_credential(account_name, account_password):
    '''
    method that creates  new  account _name
    '''
    new_credential = Credentials(account_name, account_password)

    return new_credential


def save_new_credential(credentials):
    '''
    method to save new credentials
    '''

    credentials.save_credentials()



def(main):


if __name__ == '__main__':

    main()
