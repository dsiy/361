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


class CourseTime(models.Model):
    department = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)



class InputManager:
    def command(self, command):
        output = command
        commands = command.split()
        first = commands[0].lower()
        # login
        if first == "login":
            # check size of inputs
            #a = CourseTimeValidator()
            # if a.validate(command):
            output = "login successful"
            # check email and password
            output = "login failed"

        # logout
        if first == "logout":
            # do thing
            if Account.Logout():
                output = "logout successful"

        if first == "AddClass":
          #  a = CourseTimeValidator()
           # if a.validate(command):
                output = "Class Successfully Added!"
        # create class command
        return output










class CourseTimeValidator:  # takes in string. addClass <1> <2> <3>...<n>
    def validator(self, input):
        output = True
        list = input.split()
        if not len(list) == 7 | list.len() == 8:
            output = False

        count = 0
        for a in list:
            if count == 0:
                count += 1

            elif count == 1:
                if (a.isnumeric()) == True:
                    output = False
                count += 1

            elif count == 2:
                if a.isalpha() == True:
                    output = False
                count += 1

            elif count == 3:
                if a.isalpha() == True:
                    output = False
                count += 1

            elif count == 4:
                if a.isalpha() == True:
                    output = False
                count += 1

            elif count == 5:
                if (a.isnumeric()) == True:
                    output = False
                count += 1

            elif count == 6:
                if a.isalpha() == True:
                    output = False
                count += 1

        return output