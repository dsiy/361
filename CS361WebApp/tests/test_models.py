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
        self.assertEqual(boyland.addClass("CS361" ), True)
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

    def testAccountEmailexists(self):
        test = Account.objects.get(email="krampert@uwm.edu")
        self.assertEquals(test.email, "krampert@uwm.edu")

    def test_TA_classList1(self):  # add one class
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertIs(krampert.addClass(self, "CS361", 1), True)

    def test_TA_classlist2(self):  # remove one class but no class to remove
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.removeClass(self, "CS361"), False)

    def test_TA_classlist3(self):  # add one class then remove that class
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)

    def test_TA_classlist4(self):  # add two classes and then try to add the same class again
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS395", 3), False)

    def test_TA_classlist5(self):  # add two and remove two classes
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)

    def test_TA_classlist6(self):  # add two and remove same class twice
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "cs337", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.removeClass(self, "cs337"), False)

    def test_TA_classlist7(self):  # add two classes, then remove one and add it back again
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.addClass(self, "CS395", 2), True)

    def test_TA_classlist8(self):  # add two classes, then remove two and check priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)
        self.assertEqual(krampert.viewPriorityList(self), False)

    def test_TA_classlist9(self):  # add three classes, then remove one, change priorities, and check priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS337", 1), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist10(self):  # add two classes and check priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist11(self):  # add three classes, change priorities, and check priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), False)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.changePriority(self, "CS337", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS395", 3), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist12(self):  # add two classes and change priorities
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.addClass(self, "CS431", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS431", 1), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist13(self):  # add one class and change priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), False)

    def test_TA_classlist14(self):  # add three classes, remove three, and check priority
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)
        self.assertEqual(krampert.viewPriorityList(self), False)

    def test_TA_classlist15(self):  # add four classes, check priority, remove two, and check priority again
        Account.objects.create(email="krampert@uwm.edu", password="")
        krampert = Account.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.addClass(self, "CS431", 4), True)
        self.assertEqual(krampert.viewPriorityList(self), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_priority_create1(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santa.viewPriority(), list)

    def test_TA_priority_create2(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "cS337", "CS395"]
        self.assertEqual(santha.addClass("cs361", 1), True)
        self.assertEqual(santha.addClass("cS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santa.viewPriority(), list)

    def test_TA_priority_create3(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS361", 1), False)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.addClass("cs361", 1), True)
        self.assertEqual(santha.addClass("CS420", 2), False)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santa.viewPriority(), list)

    def test_TA_priority_view_empty(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view1(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view2(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_overlap(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_remove1(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.removeClass("CS337"), True)
        self.assertEqual(santha.removeClass("CS395"), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_remove2(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.removeClass("CS361"), False)
        self.assertEqual(santha.removeClass("CS337"), True)
        self.assertEqual(santha.removeClass("CS395"), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_remove3(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.removeClass("CS420"), False)
        self.assertEqual(santha.removeClass("CS337"), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_change1(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS395", "CS337"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS 395", 3), True)
        self.assertEqual(santha.changePriority("CS 337", 2), True)
        self.assertEqual(santha.changePriority("CS 361", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_change2(self):
        TA.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = TA.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS 361", 1), True)
        self.assertEqual(santha.changePriority("CS 337", 1), True)
        self.assertEqual(santha.changePriority("CS 395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

class InstructorTestCase(TestCase):
    pass
