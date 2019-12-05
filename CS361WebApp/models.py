from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    TA = 1
    INSTRUCTOR = 2
    ADMINISTRATOR = 3
    ROLE_CHOICES = (
        (TA, 'TA'),
        (INSTRUCTOR, 'Instructor'),
        (ADMINISTRATOR, 'Administrator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    myList = models.TextField(null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class PriorityList(User):
    myList = models.TextField(null=True)


class CourseTime(models.Model):
    department = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.department + " " + self.number


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
