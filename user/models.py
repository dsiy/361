from django.db import models
from django.contrib.auth.models import User
from user.choices import *
from django.db.models import CASCADE


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

