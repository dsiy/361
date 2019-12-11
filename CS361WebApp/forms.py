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


class PriorityInit(ModelForm):
    class Meta:
        model = models.SavePriority
        fields = ['department', 'number', 'section', 'priority']

