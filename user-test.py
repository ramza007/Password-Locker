import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    test class for behaviours


    Args:
        unittest.TestCase :Test case that helps in creating test cases

    '''

    def setUp(self):
        '''
        method run before each test case
        '''

        self.new_user = User("ramza", "password")

    def test_init_(self):
        '''
        test case to if the User object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "ramza")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        '''
        test case to check if the user is able to save data
        '''
        # This saves a new user
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
