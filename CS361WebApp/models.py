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

    def get_password(self):
        return self.password


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
            elif (Account.objects.filter(email=commands[1]).exists() &
                  (Account.objects.get(email='hojin@uwm.edu').get_password() != commands[2])):
                output = "Your password is incorrect!"
            elif loggedIn.objects.filter(email=commands[1]).exists():
                output = "You are already logged in!"
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

        if first == "addClass":
            cv = CourseTimeValidator()
            if cv.validator(command):
                output = "Class successfully created!"
            else:
                output = "Invalid Class!"
        # just for checking
        output =  str(loggedIn.objects.all()) + "   " + output
        # if loggedIn.objects.all(): output = 'wahhh!!'

        # create class command
        return output


class CourseTimeValidator:  # takes in string. addClass <1> <2> <3>...<n>
    def validator(self, inputString):
        output = True
        arr = inputString.split()
        if not (len(arr) == 7 | len(arr) == 8):
            output = False

        for count, a in enumerate(arr):
            if count == 0:
                pass
            elif count == 1:
                if a.isnumeric():
                    output = False

            elif count == 2:
                if a.isalpha():
                    output = False

            elif count == 3:
                if a.isalpha():
                    output = False

            elif count == 4:
                if a.isalpha():
                    output = False

            elif count == 5:
                if a.isnumeric():
                    output = False

            elif count == 6:
                if a.isalpha():
                    output = False

        if output % len(arr) == 8:
            CourseTime(department=arr[1], number=arr[2], start=arr[3], end=arr[4],
                       day=arr[5], section=arr[6], instructor=arr[7]).save()
        elif output % len(arr) == 7:
            CourseTime(department=arr[1], number=arr[2], start=arr[3], end=arr[4],
                       day=arr[5], section=arr[6]).save()

        return output
