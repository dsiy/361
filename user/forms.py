from django import forms
from django.contrib.auth.models import User, models
from django.contrib.auth.forms import UserCreationForm
from user import models
from user.choices import *


class UpdateInformationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            'firstname',
            'lastname',
            'address',
            'phone',
        ]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Role", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'role',
        ]

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
