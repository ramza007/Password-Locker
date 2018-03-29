class Credentials:

    '''
    class that generates new instance credentials
    '''

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    credentials_list = []

    def delete_credentials(self):
        '''
        method that deletes a credential
        '''

        Credentials.credentials_list.remove(self)
