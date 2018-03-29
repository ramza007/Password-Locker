import unittest
from credentials import Credentials 


class TestCredentials(unittest.TestCase):

    '''
    test class that defines test cases for  the credentials class
    '''

    def setUp(self):
        '''
        set up method  that runs before each test case
        '''

        self.new_credentials = Credentials("Google", "3344")

    def tearDown(self):
        '''
         tear down method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_credentials_instance(self):
        '''
        method to test if new credentials have been instanciated properly
        '''

        self.assertEqual(self.new_credentials.account_name, "Google")
        self.assertEqual(self.new_credentials.account_password, "3344")

    def test_save_credentials(self):
        '''
        test case to test if credentials objects have been saved into user_list
        '''

        self.new_credentials.save_credentials()  # save new user
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_delete_credentials(self):
        '''
        test delete credentials to test if we can remove a account from our list
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Google", "3344")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()  # to delete a credentials   object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a credentials by the account name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Google", "3344")
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_number("0711491808")
        self.assertEqual(found_credentials.credentials_name,
                         test_credentials.password)

    def test_display_all_credentials(self):
        """TestCase to test whether all contacts can be displayed"""
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)


if __name__ == '__main__':
   unittest.main()
