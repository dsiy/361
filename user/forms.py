from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile
from user.choices import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Role", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
