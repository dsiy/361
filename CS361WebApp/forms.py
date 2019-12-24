from django import forms
from django.forms import ModelForm, ModelChoiceField, CharField
from CS361WebApp import models
from user.models import Profile
from django.db.models import Q


class CourseTimeForm(ModelForm):
    class Meta:
        model = models.CourseTime
        fields = ['department', 'number', 'start', 'end', 'day', 'section', 'instructor']


class AssignUserForm(forms.Form):
    course = ModelChoiceField(queryset=models.CourseTime.objects.all())
    instructor = ModelChoiceField(queryset=Profile.objects.filter(Q(role=1) | Q(role=2)))


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
