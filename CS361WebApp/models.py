from django.core.exceptions import ObjectDoesNotExist
from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    loggedIn = models.BooleanField(default=False)

    # Returns True if account was succesfully logged in
    # Throws an error is the account is not valid
    def login(self, password):

        if self.password != password:
            output = "Your password is incorrect!"

        elif self.loggedIn:
            output = "You are already logged in!"

        else:
            # add to loggedIn table v
            self.loggedIn = True
            self.save()
            output = "Log-in Success!"

        return output

    def logout(self):
        if not self.loggedIn:
            output = "You are not logged in!"
        else:
            self.loggedIn = False
            self.save()
            output = "Log-out Success!"

        return output

    def __str__(self):
        return self.email

    def get_password(self):
        return self.password


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

    def addClass(self, className, priority):
        pass

    def viewPriorityList(self):
        pass

    def changePriority(self, className, priority):
        pass

    def removeClass(self, className):
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
    instructor = models.CharField(max_length=50, blank = True)


class InputManager:
    def command(self, command):
        output = command
        commands = command.split()
        first = commands[0].lower()

        # login
        if first == "login":
            # check size of inputs v
            # check email and password v
            # check if there is duplicate v

            if (len(commands) < 3) | (not Account.objects.filter(email=commands[1]).exists()):
                output = "No Such User Exists!"
            elif Account.objects.filter(email=commands[1]).exists():
                try:
                    output = Account.objects.filter(email=commands[1])[0].login(commands[2])
                except Account.DoesNotExist:
                    output = "No Such User Exists!"
        # logout
        if first == "logout":
            # if logged in
            if len(commands) < 2 | (not Account.objects.filter(email=commands[1]).exists()):
                output = "No Such User Exists!"
            else:
                output = Account.objects.filter(email=commands[1])[0].logout()

        if first == "addClass":
            cv = CourseTimeValidator()
            if cv.validator(command):
                output = "Class successfully created!"
            else:
                output = "Invalid Class!"
        # just for checking
        # output =  str(loggedIn.objects.all()) + "   " + output
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
