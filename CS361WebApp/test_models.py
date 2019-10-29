from django.test import TestCase
from CS361WebApp.models import Account, Administrator, TA, Instructor
class AccountTestCase(TestCase):
    def setUp(self):
        testAccount = Account(email="", password="")
    def testAccountEmail(self):
        testAccount = Account(email="", password="")
        self.assertEquals(testAccount.email, "radojev3@uwm.edu")

class AdministratorTestCase(TestCase):
    pass

class TATestCase(TestCase):
    pass

class InstructorTestCase(TestCase):
    pass