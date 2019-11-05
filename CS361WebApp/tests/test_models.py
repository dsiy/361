from django.test import TestCase
from CS361WebApp.models import Account, Administrator, TA, Instructor


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(email="radojev3@uwm.edu", password="")

    def testAccountEmailexists(self):
        test = Account.objects.get(email="radojev3@uwm.edu")
        self.assertEquals(test.email, "radojev3@uwm.edu")

class AdministratorTestCase(TestCase):

    def test_account_login1(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertIs(boyland.login("unbreakable"), True)

    def test_account_login2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertRaises(boyland.login("wrongPassword"), "InvalidPasswordException")

    def test_account_logout1(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        boyland.login("unbreakable")
        self.assertEqual(boyland.logout(), True)

    def test_account_logout(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.logout(), False)

    def test_admin_classList1(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        Administrator.objects.create(boyland)
        boylandAdmin = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertIs(boylandAdmin.addClass(name="CS361"), True)

    def test_admin_classlist2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        Administrator.objects.create(boyland)
        boylandAdmin = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertIs(boylandAdmin.removeClass(name="CS361"), False)

    def test_admin_classlist3(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        Administrator.objects.create(boyland)
        boylandAdmin = Administrator.objects.get(email="boyland@uwm.edu")
        boylandAdmin.addClass(name="CS361")
        self.assertIs(boylandAdmin.removeClass(name="CS361"), False)


class TATestCase(TestCase):
    pass


class InstructorTestCase(TestCase):
    pass
