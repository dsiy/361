from django.test import TestCase
from CS361WebApp.models import Account, Administrator, TA, Instructor


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(email="radojev3@uwm.edu", password="")

    def testAccountEmailexists(self):
        test = Account.objects.get(email="radojev3@uwm.edu")
        self.assertEquals(test.email, "radojev3@uwm.edu")

    def test_account_emailNotExist2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.email, "boyland@uwm.edu")

    def test_account_login1(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def testAccountLogin2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def test_account_login2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("wrongPassword"), False)

    def test_account_login3(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        Account.objects.create(email="boyland2@uwm.edu", password="unbreakable2")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        boyland2 = Account.objects.get(email="boyland2@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def test_account_logout1(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)
        self.assertEqual(boyland.logout(), True)

    def test_account_logout2(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.logout(), False)

    def test_account_logout3(self):
        Account.objects.create(email="boyland@uwm.edu", password="unbreakable")
        Account.objects.create(email="blank", password="blank")
        boyland = Account.objects.get(email="boyland@uwm.edu")
        blank = Account.objects.get(email="blank")
        self.assertEqual(boyland.login("unbreakable"), True)
        self.assertEqual(blank.logout(), False)


class AdministratorTestCase(TestCase):

    def test_admin_classList1(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertIs(boyland.addClass("CS361"), True)

    def test_admin_classlist2(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.removeClass("CS361"), False)

    def test_admin_classlist3(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS361"), True)

    def test_admin_classlist4(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.addClass("CS395"), False)

    def test_admin_classlist5(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS395"), True)
        self.assertEqual(boyland.removeClass("CS361"), True)

    def test_admin_classlist6(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("cs361"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS361"), True)
        self.assertEqual(boyland.removeClass("cs361"), True)

    def test_admin_classlist5(self):
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Administrator.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS395"), False)

class TATestCase(TestCase):
    pass


class InstructorTestCase(TestCase):
    pass
