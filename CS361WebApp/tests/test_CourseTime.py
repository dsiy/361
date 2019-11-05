from django.test import TestCase
from CS361WebApp.models import Account, Administrator, TA, Instructor, CourseTime


class CourseTimeTest(TestCase):

    def setUp(self):
        pass

    # Returns True or False.
    def test_init1(self):
        time = CourseTime
        with self.assertRaises(TypeError):
            time.__init__("")

    # Returns True or False.
    def test_init2(self):
        time = CourseTime
        with self.assertRaises(TypeError):
            time.__init__(2)

    # Returns True or False.
    def test_init3(self):
        time = CourseTime
        time.__init__("online")
        self.assertEqual(time.start, "midnight")
        self.assertEqual(time.end, "midnight")
        self.assertEqual(time.day, None)

    # Returns True or False.
    def test_init4(self):
        time = CourseTime
        with self.assertRaises(TypeError):
            time.__init__("9000 1100 S")

    # Returns True or False.
    def test_str1(self):
        time = CourseTime
        time.__init__("online")
        self.assertEqual(time.__str__(), "online")

    # Returns True or False.
    def test_str2(self):
        time = CourseTime
        time.__init__("9000 1100 M")
        self.assertEqual(time.__str__(), "9000 1100 M")

    # Returns True or False.
    def test_start(self):
        time = CourseTime
        time.__init__("9000 1100 M")
        self.assertEqual(time.start, "9000")
        self.assertNotEqual(time.start, "1100")

    # Returns True or False.
    def test_end(self):
        time = CourseTime
        time.__init__("9000 1100 M")
        self.assertEqual(time.start, "1100")
        self.assertNotEqual(time.start, "9000")

    # Returns True or False.
    def test_isOnline1(self):
        time = CourseTime
        time.__init__("online")
        self.assertTrue(time.isOnline, True)

    # Returns True or False.
    def test_isOnline2(self):
        time = CourseTime
        time.__init__("9000 1100 M")
        self.assertTrue(time.isOnline, False)

    # Returns True or False.
    def test_isOverlap1(self):
        time = CourseTime
        time2 = CourseTime
        time.__init__("9000 1100 M")
        time2.__init__("1000 1200 M")
        self.assertTrue(time.isOverlap(time2), True)
        self.assertTrue(time2.isOverlap(time), True)

    # Returns True or False.
    def test_isOverlap2(self):
        time = CourseTime
        time2 = CourseTime
        time.__init__("9000 1100 M")
        time2.__init__("online")
        self.assertTrue(time.isOverlap(time2), False)
        self.assertTrue(time2.isOverlap(time), False)

    def test_account_login1(self):
        Account.object.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.get(email="boyland@uwm.edu")
        self.assertIs(boyland.Login("unbreakable"), True)

    def test_account_login2(self):
        Account.object.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.get(email="boyland@uwm.edu")
        self.assertRaises(boyland.login("wrongPassword"), "InvalidPasswordException")

    def test_account_logout1(self):
        Account.object.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.get(email="boyland@uwm.edu")
        boyland.Login("unbreakable")
        self.assertEqual(boyland.Logout(), True)

    def test_account_logout(self):
        Account.object.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.Logout(), False)

    def test_admin_classList1(self):
        Account.object.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = Account.get(email="boyland@uwm.edu")
        Administrator.object.create(email="boyland@uwm.edu", password="unbreakable")
        boylandAdmin = Administrator.get(email="boyland@uwm.edu")
        boylandAdmin.addClass(name="CS361")





if __name__ == '__main__':
    unittest.main()


