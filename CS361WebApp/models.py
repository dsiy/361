from django.db import models

# Create your models here.
class YourClass:
  def command(self,inStr):
    return inStr

class Account(models.Model):
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  def Login(self):
    pass
  def Logout(self):
    pass

class Administrator(Account):
  def resetPassword(self):
    pass
  def addClass(self):
    pass
  def removeClass(self):
    pass

class TA(Account):
  def fill_Info(self):
    pass

class Instructor(Account):
  pass


