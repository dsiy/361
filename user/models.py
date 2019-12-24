from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from user.choices import *
from django.db.models.signals import post_save
from django.db.models import CASCADE


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):  # unicode for Python 2
        return self.user.username


@receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# post_save.1(create_user_profile, sender=User)
