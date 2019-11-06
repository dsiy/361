from django.core.exceptions import ObjectDoesNotExist
from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    # Returns True if account was succesfully logged in
    # Throws an error is the account is not valid
    def login(self, password):
        pass

    def logout(self):
        pass

    def __str__(self):
        return self.email


class loggedIn(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


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
            # check size of inputs v
            # check email and password v
            # check if there is duplicate
            if (len(commands) < 3) | (not Account.objects.filter(email=commands[1]).exists()):
                output = "No Such User Exists!"
            else:
                # add to loggedIn table v
                comein = loggedIn(email=commands[1])
                comein.save()
                output = "Log-in Success!"


        # logout
        if first == "logout":
            # do thing
            if ((not Account.objects.filter(email=commands[1]).exists())
                    | (not loggedIn.objects.filter(email=commands[1]).exists())):
                output = "You are not logged in!"
            else:
                getout = loggedIn.objects.get(email=commands[1])
                getout.delete()
                output = "Log-out Success!"
        # just for checking
        output = loggedIn.objects.all()
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