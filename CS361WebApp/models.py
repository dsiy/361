from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from CS361WebApp.validator import *

# Create your models here.
from django.template.defaultfilters import slugify


class CourseTime(models.Model):
    department = models.CharField(max_length=50, validators=[validate_alpha])
    number = models.CharField(max_length=50, validators=[validate_numeric])
    start = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    end = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    day = models.CharField(max_length=50, validators=[validate_alpha])
    section = models.CharField(max_length=50, validators=[validate_numeric])
    instructor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.department + " " + self.number + "-" + self.section


class CreatePriority(models.Model):
    classes = models.ForeignKey('CourseTime', on_delete=CASCADE, null=True)
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])

    def __str__(self):
        return self.classes.department + " " + self.classes.number + " " + self.classes.section + " " + self.priority


class SavePriority(models.Model):
    user = models.CharField(max_length=30, null=True, blank=True)
    myList = models.ManyToManyField(CreatePriority)

    class Meta:
        ordering = ['user']

    def __str__(self):
        x = self.myList.all()
        string = ""
        for values in x:
            string = string + str(values) + " "
        return string


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
