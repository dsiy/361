from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    # Returns True if account was succesfully logged in
    # Throws an error is the account is not valid
    def Login(self, password):
        pass

    def Logout(self):
        pass


class Administrator(Account):
    def resetPassword(self):
        pass

    # Returns True if class was successfully added to the classList and False if there is an error adding the class
    def addClass(self, className):
        pass

    # Returns True if class was successfully removed to the classList and False if there is an error removing the class
    def removeClass(self, className):
        pass


class TA(Account):
    def fill_Info(self):
        pass


class Instructor(Account):
    pass


# classList model needs to be added here

class InputManager:
    def command(self, command):
        output = command
        commands = command.split()
        first = commands[0].lower()
        # login
        if first == "login":
            # check size of inputs
            # check email and password
            output = "login successful"
            output = "login failed"

        # logout
        if first == "logout":
            # do thing
            output = "logout successful"

        # create class command
        return output
