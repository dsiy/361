from django.db import models

# Create your models here.
class MyModel(models.Model):

    fieldOne = models.CharField(max_length=20, null=False, default='Z')
    fieldTwo = models.IntegerField(null=False, default='10')
    color = models.CharField(max_length=7)

