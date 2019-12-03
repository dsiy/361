from django import forms
from django.forms import ModelForm
from CS361WebApp import models

class CourseTimeForm(ModelForm):
	class Meta:
		model = models.CourseTime
		fields = ['department', 'number', 'start', 'end', 'day', 'section', 'instructor']