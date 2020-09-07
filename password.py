class User:
            def __init__(self, first_name, last_name, phone_number, email):
                self.first_name = first_name
                self.last_name = last_name
                self.phone_number = phone_number
                self.email = email

            password_list = []

            def save_password(self):
                User.password_list.append(self)

            def delete_password(self):
                User.password_list.remove(self)

            @classmethod
            def find_by_number(cls, number):
                '''
                  Method that takes in a number and returns a password that matches that number.
                  Args:if
                      number: Phone number to search for
                  Returns :
                     password of person that matches the number.
                  '''
                for password in cls.password_list:
                    if password.phone_number == number:
                        return password

            @classmethod
            def password_exist(cls, number):
                '''
                Method that checks if a password exists from the password list.
                Args:
                    number: Phone number to search if it exists
                Returns :
                    Boolean: True or false depending if the password exists
                '''
                for password in cls.password_list:
                    if password.phone_number == number:
                        return True
                return False

            @classmethod
            def display_passwords(cls):
                '''
                method that returns the password list
                '''
                return cls.password_list
