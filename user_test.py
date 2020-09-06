import unittest
import pyperclip


from password import User

class TestUser(unittest.TestCase):


    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = User("Charles", "Osango", "0746170913", "charlesosango02@gmail.com")  # create contact object

        # setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.password_list = []

        # other test cases here
    def test_save_multiple_password(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_password.save_password()
        test_password = User("Test", "user", "0746170913", "charlesosango02@gmail.com")  # new contact
        test_password.save_password()
        self.assertEqual(len(User.password_list), 2)

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name, "Charles")
        self.assertEqual(self.new_password.last_name, "Osango")
        self.assertEqual(self.new_password.phone_number, "0746170913")
        self.assertEqual(self.new_password.email, "charlesosango02@gmail.com")

    def test_save_password(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_password.save_password()  # saving the new contact
        self.assertEqual(len(User.password_list), 1)

        # Items up here...

    def test_save_multiple_password(self):
        '''
        test_save_multiple_contact to chec
        k if we can save multiple contact
        objects to our contact_list
        '''
        self.new_password.save_password()
        test_password = User("Test", "user", "0746170913", "charlesosango02@gmail.com")  # new contact
        test_password.save_password()
        self.assertEqual(len(User.password_list), 2)

        # More tests above
    def test_delete_password(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_password.save_password()
        test_password = User("Test", "user", "0746170913", "charlesosango02@gmail.com")  # new contact
        test_password.save_password()

        self.new_password.delete_password()  # Deleting a contact object
        self.assertEqual(len(User.password_list), 1)

    def test_find_password_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_password.save_password()
        test_password = User("Test", "user", "074617", "charlesosango02@gmail.com")  # new contact
        test_password.save_password()

        found_password =User.find_by_number("0746170913")

        self.assertEqual(found_password.email, test_password.email)


    def test_password_exists(self):
         '''
         est to check if we can return a Boolean  if we cannot find the contact.
         '''

         self.new_password.save_password()
         test_password = User("Test","user","0746170913","charlesosango02@gmail.com") # new contact
         test_password.save_password()

         contact_exists = User.password_exist("0746170913")


    def test_display_all_passwords(self):
          '''
          method that returns a list of all contacts saved
          '''

          self.assertEqual(User.display_passwords(),User.password_list)

    # def test_copy_email(self):
    #      '''
    #      Test to confirm that we are copying the email address from a found contact
    #      '''
    #
    #      self.new_user.save_user()
    #      User.copy_email("0712345678")
    #
    #      self.assertEqual(self.new_user.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()