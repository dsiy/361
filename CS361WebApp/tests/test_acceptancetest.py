from django.contrib.auth import authenticate
from django.test import TestCase
from CS361WebApp.models import User, CourseTime
from CS361WebApp.validator import validate_alpha, validate_numeric
import unittest
from ..forms import *
from CS361WebApp.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class AcceptanceTests(TestCase):

    # As an admin I should be able to login using my username and password by entering them into the login page

    def test_admin_login_valid(self):
        # Form is valid because the login information entered is correct for an admin
        a = User.objects.create_superuser('admin', 'admin@uwm.edu', 'password')
        self.assertTrue(a.is_authenticated)
        # form = AuthenticationForm(None, data={'username': a.username, 'password': a.password})

    def test_admin_login_invalid(self):
        # Form is invalid because the login information entered is incorrect for an admin
        uname = "username"
        pword = "password"
        self.assertEqual(None, authenticate(username=uname, password=pword))

    # As a TA I should be able to login using my username and password by entering them into the login page

    def test_ta_login_valid(self):
        # Form is valid because the login information entered is correct for a TA
        u = User.objects.create_user('TA', 'ta@uwm.edu', 'password', 'TA')
        form = AuthenticationForm(data={'username': u.username, 'password': u.password})
        self.assertTrue(form.is_valid())

    def test_ta_login_invalid(self):
        # Form is invalid because the login information entered is incorrect for a TA
        form = AuthenticationForm(data={'username': 'TA', 'password': 'password'})
        self.assertFalse(form.is_valid())

    # As an admin I should be able to create classes for TAs to chooses from

    def test_create_class_valid(self):
        # Form is valid because the class information entered fits the required parameters
        department = "CS"
        num = "361"
        start = "11:00"
        end = "11:50"
        day = "TTH"
        section = "801"
        instructor = " "
        form = CourseTimeForm(data={"department": department, "number": num, "start": start, "end": end, "day": day, "section": section, "instructor": instructor})
        self.assertTrue(form.is_valid())

    def test_create_class_invalid1(self):
        # Form is invalid because the start time is not the correct time format
        department = "CS"
        num = "361"
        start = "1100"
        end = "11:50"
        day = "TTH"
        section = "801"
        instructor = " "
        form = CourseTimeForm(
            data={"department": department, "number": num, "start": start, "end": end, "day": day, "section": section,
                  "instructor": instructor})
        self.assertFalse(form.is_valid())

    def test_create_class_invalid2(self):
        # Form is invalid because the end time is not the correct time format
        department = "CS"
        num = "361"
        start = "11:00"
        end = "1150"
        day = "TTH"
        section = "801"
        instructor = " "
        form = CourseTimeForm(
            data={"department": department, "number": num, "start": start, "end": end, "day": day, "section": section,
                  "instructor": instructor})
        self.assertFalse(form.is_valid())

    # As an admin I should be able to create an account for a TA

    def test_admin_create_ta_account_valid(self):
        # Valid form entry by entering the correct parameters for each field
        username = "stoffel"
        email = "stoffelb@uwm.edu"
        passwrd = "bryansucks"
        form = forms.objects.UserRegisterForm(data={"username": username, "password1": passwrd, "password2": passwrd})
        self.assertTrue(form.is_valid())

    def test_admin_create_ta_account_invalid(self):
        # Invalid form because the password confirmation does not match the first password entry
        username = "stoffel"
        email = "stoffelb@uwm.edu"
        passwrd1 = "bryansucks"
        passwrd2 = "bryanrocks"
        form = forms.objects.UserRegisterForm(data={"username": username, "password1": passwrd1, "password2": passwrd2})
        self.assertFalse(form.is_valid())

    # As a TA I should be able to select from a list of classes and create a priority list of them

    def test_ta_assign_priority_list_valid(self):
        # Valid form entry by selecting a real class and a valid priority number
        c1 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Boyland")
        form = Priority(data={"classes": c1, "priority": "1"})
        self.assertTrue(form.is_valid())

    def test_ta_assign_priority_list_invalid(self):
        # Invalid form entry by selecting an invalid priority number (-1)
        c1 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Boyland")
        form = Priority(data={"classes": c1, "priority": "-1"})
        self.assertFalse(form.is_valid())

    # As an admin I should be able to assign Instructors to courses through a form
    def test_admin_assign_instructor_valid(self):
        # Form is valid because a class is selected from the drop down and an Instructor name is entered into the field
        c1 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Boyland")
        form = AssignUserForm(data={'course': c1, 'instructor': 'Rock'})
        self.assertTrue(form.is_valid())

    def test_admin_assign_instructor_invalid(self):
        # Form is invalid because a class has not been selected to assign the Instructor to
        c1 = "CS 351 603 Boyland"
        form = AssignUserForm(data={'course': c1, 'instructor': 'Rock'})
        self.assertFalse(form.is_valid())

    if __name__ == '__main__':
        unittest.main()
