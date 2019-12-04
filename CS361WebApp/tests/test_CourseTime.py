
from django.test import TestCase
from CS361WebApp.models import User, CourseTime, CourseTimeValidator


class CourseTimeTest(TestCase):

    def setUp(self):
        pass

    # Returns True or False.
    def test_init1(self):
        time = CourseTimeValidator.validator("")
        self.assertEquals(time, False);

    # Returns True or False.
    def test_init2(self):
        time = CourseTimeValidator.validator("addClass CS351")
        self.assertEquals(time, False)

    # Returns True or False.
    def test_init3(self):
        time = CourseTime.objects.create(start="midnight", end="midnight", day=None);
        self.assertEqual(time.start, "midnight")
        self.assertEqual(time.end, "midnight")
        self.assertEqual(time.day, None)

    # Returns True or False.
    def test_init4(self):
        time = CourseTimeValidator.validator("addClass compsci 351 9000 1100 S 801 Rock")
        self.assertEquals(time, True)

    # Returns True or False.
    def test_str1(self):
        time = CourseTimeValidator.validator("addClass compsci 341 0000 0000 S 801 Rock")
        self.assertEquals(time, True)

    # Returns True or False.
    def test_str2(self):
        time = CourseTimeValidator.validator("addClass busadmin 351 9000 1100 S 801")
        self.assertEquals(time, True)

    # Returns True or False.
    def test_start(self):
        time = CourseTime.objects.create(department= "compsci", start= 9000)
        self.assertEqual(time.start, "9000")
        self.assertNotEqual(time.start, "1100")

    # Returns True or False.
    def test_end(self):
        time = CourseTime.objects.create(department= "compsci", start= 1100)
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
        self.assertTrue(time.objects.isOnline, False)

    # Returns True or False.
    def test_isOverlap1(self):
        time = CourseTime
        time2 = CourseTime
        time.__init__("9000 1100 M")
        time2.__init__("1000 1200 M")
        self.assertTrue(time.objects.isOverlap(time2), True)
        self.assertTrue(time2.objects.isOverlap(time), True)

    # Returns True or False.
    def test_isOverlap2(self):
        time = CourseTime
        time2 = CourseTime
        time.__init__("9000 1100 M")
        time2.__init__("online")
        self.assertTrue(time.objects.isOverlap(time2), False)
        self.assertTrue(time2.objects.isOverlap(time), False)

    def test_User_login1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertIs(boyland.Login("unbreakable"), True)

    def test_User_login2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertRaises(boyland.login("wrongPassword"), "InvalidPasswordException")

    def test_User_logout1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        boyland.Login("unbreakable")
        self.assertEqual(boyland.Logout(), True)

    def test_User_logout(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEqual(boyland.Logout(), False)

    def test_admin_classList1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        Administrator.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boylandAdmin = Administrator.objects.get(email="boyland@uwm.edu")
        boylandAdmin.addClass(name="CS361")


if __name__ == '__main__':
    unittest.main()
