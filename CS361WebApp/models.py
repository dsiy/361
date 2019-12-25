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
