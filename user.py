class User:

    '''
    class that generates new instance of user
    '''

    user_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves a new user objects to the user_list
        '''

        User.user_list.append(self)
