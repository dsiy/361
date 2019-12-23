from django.test import TestCase
from CS361WebApp.models import User, CourseTime
from CS361WebApp.validator import validate_alpha, validate_numeric
import unittest
from ..forms import *
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AcceptanceTests(TestCase):


    def test_acceptance_validator1(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha('2'))

    def test_acceptance_validator2(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha('%'))

    def test_acceptance_validator3(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha(3))

    def test_acceptance_validator4(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha('hell0'))

    def test_acceptance_validator5(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha())

    def test_acceptance_validator6(self):
        # validate alphabetic
        self.assertraises('data must not contain numbers or symbols', validate_alpha(' '))

    def test_acceptance_validator7(self):
        # validate number
        self.assertraises('data must be comprised only of numbers', validate_numeric(''))

    def test_acceptance_validator8(self):
        # validate number
        self.assertraises('data must be comprised only of numbers', validate_numeric('678h'))

    def test_acceptance_validator9(self):
        # validate number
        self.assertraises('data must be comprised only of numbers', validate_numeric('6%'))

    def test_acceptance_validator10(self):
        # validate number
        self.assertraises('data must be comprised only of numbers', validate_numeric('  6'))



    def test_admin_create_ta_account(self):

        # As an admin I should be able to create an account for a TA
        username = "stoffel"
        email = "stoffelb@uwm.edu"
        passwrd = "bryansucks"
        form = forms.objects.UserRegisterForm(data={"username": username, "password1": passwrd, "password2": passwrd})
        self.assertTrue(form.is_valid())

    def test_admin_create_professor_account(self):

        # As an admin I should be able to create an account for a professor
        username = "stoffel"
        email = "stoffelb@uwm.edu"
        passwrd1 = "bryansucks"
        passwrd2 = "bryanrocks"
        form = forms.objects.UserRegisterForm(data={"username": username, "password1": passwrd1, "password2": passwrd2})
        self.assertFalse(form.is_valid())




if __name__ == '__main__':
    unittest.main()
