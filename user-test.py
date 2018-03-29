import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviors


    Args:
        unittest.TestCase :Test case that helps in creating test cases

    '''

    def setUp(self):
        '''
        method to run before each test case
        '''

        self.new_user = User("ramza", "password")

    def test_init_(self):
        '''
        test case to if the User object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "ramza")
        self.assertEqual(self.new_user.password, "password")
