from django.test import TestCase
from CS361WebApp.models import User, CourseTime, CreatePriority, SavePriority


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="radojev3@uwm.edu", password="")

    def testUserEmailexists(self):
        test = User.objects.get(email="radojev3@uwm.edu")
        self.assertEquals(test.email, "radojev3@uwm.edu")

    def test_User_emailNotExist2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.email, "boyland@uwm.edu")

    def test_User_login1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def testUserLogin2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def test_User_login2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("wrongPassword"), False)

    def test_User_login3(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        User.objects.create(email="boyland2@uwm.edu", password="unbreakable2")
        boyland = User.objects.get(email="boyland@uwm.edu")
        boyland2 = User.objects.get(email="boyland2@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)

    def test_User_logout1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.login("unbreakable"), True)
        self.assertEqual(boyland.logout(), True)

    def test_User_logout2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.logout(), False)

    def test_User_logout3(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        User.objects.create(email="blank", password="blank")
        boyland = User.objects.get(email="boyland@uwm.edu")
        blank = User.objects.get(email="blank")
        self.assertEqual(boyland.login("unbreakable"), True)
        self.assertEqual(blank.logout(), False)


class UserTestCase(TestCase):

    def test_admin_classList1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertIs(boyland.addClass("CS361"), True)

    def test_admin_classlist2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.removeClass("CS361"), False)

    def test_admin_classlist3(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS361" ), True)
        self.assertEqual(boyland.removeClass("CS361"), True)

    def test_admin_classlist4(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.addClass("CS395"), False)

    def test_admin_classlist5(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS395"), True)
        self.assertEqual(boyland.removeClass("CS361"), True)

    def test_admin_classlist6(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("cs361"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS361"), True)
        self.assertEqual(boyland.removeClass("cs361"), True)

    def test_admin_classlist5(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.addClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS361"), True)
        self.assertEqual(boyland.removeClass("CS395"), True)
        self.assertEqual(boyland.addClass("CS395"), False)

class TATestCase(TestCase):

    def testUserEmailexists(self):
        test = User.objects.get(email="krampert@uwm.edu")
        self.assertEquals(test.email, "krampert@uwm.edu")

    def test_TA_classList1(self):  # add one class
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertIs(krampert.addClass(self, "CS361", 1), True)

    def test_TA_classlist2(self):  # remove one class but no class to remove
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.removeClass(self, "CS361"), False)

    def test_TA_classlist3(self):  # add one class then remove that class
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)

    def test_TA_classlist4(self):  # add two classes and then try to add the same class again
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS395", 3), False)

    def test_TA_classlist5(self):  # add two and remove two classes
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)

    def test_TA_classlist6(self):  # add two and remove same class twice
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "cs337", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.removeClass(self, "cs337"), False)

    def test_TA_classlist7(self):  # add two classes, then remove one and add it back again
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.addClass(self, "CS395", 2), True)

    def test_TA_classlist8(self):  # add two classes, then remove two and check priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)
        self.assertEqual(krampert.viewPriorityList(self), False)

    def test_TA_classlist9(self):  # add three classes, then remove one, change priorities, and check priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS337", 1), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist10(self):  # add two classes and check priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist11(self):  # add three classes, change priorities, and check priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 2), False)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 1), True)
        self.assertEqual(krampert.changePriority(self, "CS337", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS395", 3), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist12(self):  # add two classes and change priorities
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.addClass(self, "CS431", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), True)
        self.assertEqual(krampert.changePriority(self, "CS431", 1), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_classlist13(self):  # add one class and change priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS361", 1), True)
        self.assertEqual(krampert.changePriority(self, "CS361", 2), False)

    def test_TA_classlist14(self):  # add three classes, remove three, and check priority
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.removeClass(self, "CS361"), True)
        self.assertEqual(krampert.viewPriorityList(self), False)

    def test_TA_classlist15(self):  # add four classes, check priority, remove two, and check priority again
        User.objects.create(email="krampert@uwm.edu", password="")
        krampert = User.objects.get(email="krampert@uwm.edu")
        self.assertEqual(krampert.addClass(self, "CS395", 1), True)
        self.assertEqual(krampert.addClass(self, "CS361", 2), True)
        self.assertEqual(krampert.addClass(self, "CS337", 3), True)
        self.assertEqual(krampert.addClass(self, "CS431", 4), True)
        self.assertEqual(krampert.viewPriorityList(self), True)
        self.assertEqual(krampert.removeClass(self, "CS395"), True)
        self.assertEqual(krampert.removeClass(self, "CS337"), True)
        self.assertEqual(krampert.viewPriorityList(self), True)

    def test_TA_priority_create1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_create2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "cS337", "CS395"]
        self.assertEqual(santha.addClass("cs361", 1), True)
        self.assertEqual(santha.addClass("cS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_create3(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS361", 1), False)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.addClass("cs361", 1), True)
        self.assertEqual(santha.addClass("CS420", 2), False)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view_empty(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_overlap(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_remove1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.removeClass("CS337"), True)
        self.assertEqual(santha.removeClass("CS395"), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_remove2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
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
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.removeClass("CS361"), True)
        self.assertEqual(santha.removeClass("CS420"), False)
        self.assertEqual(santha.removeClass("CS337"), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_change1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS395", "CS337"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS 395", 3), True)
        self.assertEqual(santha.changePriority("CS 337", 2), True)
        self.assertEqual(santha.changePriority("CS 361", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_change2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS 361", 1), True)
        self.assertEqual(santha.changePriority("CS 337", 1), True)
        self.assertEqual(santha.changePriority("CS 395", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_create_priority1(self):
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.get(classes=c361), c1)

    def test_create_priority2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.get(classes=c395), None)

    def test_create_priority3(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="3")
        self.assertEquals(CreatePriority.objects.get(priority="3"), c2)

    def test_create_priority4(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertEquals(CreatePriority.objects.get(priority="1"), c2)

    def test_create_priority5(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertNotEquals(CreatePriority.objects.get(priority="1"), c1)

    def test_create_priority5(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="one")
        self.assertNotEquals(CreatePriority.objects.get(priority="one"), None)

    def test_save_priority1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="3")
        pList = CreatePriority.objects.all()
        sp1 = SavePriority.objects.create(user=santha, myList=pList)
        self.assertEquals(SavePriority.objects.get(user=santha), sp1)

    def test_save_priority2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        User.objects.create(email="stoffleb@uwm.edu", passord="iamTA55!")
        bryan = User.objects.get(email="stoffelb@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="2")
        c3 = CreatePriority.objects.create(classes=c395, priority="3")
        sList = CreatePriority.objects.all()
        bList = CreatePriority.objects.get(classes=c361)
        sp1 = SavePriority.objects.create(user=santha, myList=sList)
        sp2 = SavePriority.objects.create(user=bryan, myList=bList)
        sp2.myList.add(c3)
        self.assertEquals(SavePriority.objects.get(user=bryan).objects.get(classes=c395), c3)

class InstructorTestCase(TestCase):
    pass
