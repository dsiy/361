from django import forms
from django.forms import ModelForm
from CS361WebApp import models


class CourseTimeForm(ModelForm):
    class Meta:
        model = models.CourseTime
        fields = ['department', 'number', 'start', 'end', 'day', 'section', 'instructor']


class AssignUserForm(ModelForm):
    class Meta:
        model = models.CourseTime
        fields = ['department', 'number', 'section', 'instructor']


class Priority(ModelForm):
    class Meta:
        model = models.CreatePriority
        fields = ['classes', 'priority']


# not sure if i need this
class PriorityList(ModelForm):
    class Meta:
        model = models.SavePriority
        fields = ['myList', 'user']
#
# class PriorityInit(ModelForm):
#     class Meta:
#         model = models.SavePriority
#         fields = ['department', 'number', 'section', 'priority']
#
