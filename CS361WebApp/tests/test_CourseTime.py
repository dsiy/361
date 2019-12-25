from django.core.exceptions import ValidationError
from django.test import TestCase
import unittest
from CS361WebApp.models import User, CourseTime, validate_course
from user.models import Profile


class CourseTimeTest(TestCase):

    def setUp(self):
        pass

    # Returns True or False.
    def test_init1(self):
        time = CourseTime.objects.create(department="CS", number="351", section="234", day="MW")
        time.number = "yeet"
        with self.assertRaises(ValidationError) as cm:
            validate_course(time)
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must be comprised only of numbers')

        # Returns True or False.

    def test_init2(self):
        time = CourseTime.objects.create(department="CS", number="351", section="234", day="MW")
        time.department = "420"
        with self.assertRaises(ValidationError) as cm:
            validate_course(time)
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    # Returns True or False.
    def test_init3(self):
        time = CourseTime.objects.create(start="23:00", end="23:00")
        self.assertEqual(time.start, "23:00")
        self.assertEqual(time.end, "23:00")
        self.assertEqual(time.day, "")

    # Returns True or False.
    def test_init4(self):
        time = CourseTime.objects.create(department="CS", number="351", section="401", start="09:00", end="09:50", day="TTR")
        self.assertTrue(validate_course(time))

    # # Returns True or False.
    # def test_str1(self):
    #     time = CourseTimeValidator.validator("addClass compsci 341 0000 0000 S 801 Rock")
    #     self.assertEquals(time, True)
    #
    # # Returns True or False.
    # def test_str2(self):
    #     time = CourseTimeValidator.validator("addClass busadmin 351 9000 1100 S 801")
    #     self.assertEquals(time, True)

    # Returns True or False.
    def test_start(self):
        time = CourseTime.objects.create(department="CS", start="09:00")
        self.assertEqual(time.start, "09:00")
        self.assertNotEqual(time.start, "11:00")

    # Returns True or False.
    def test_end(self):
        time = CourseTime.objects.create(department="CS", end="11:00")
        self.assertEqual(time.end, "11:00")
        self.assertNotEqual(time.end, "09:00")

    # Returns True or False.
    def test_isOnline1(self):
        time = CourseTime.objects.create(start="23:00")
        self.assertEqual(time.start, "23:00")

    # Returns True or False.
    def test_isOnline2(self):
        time = CourseTime.objects.create(start="09:00")
        self.assertNotEqual(time.start, "23:00")

    # Returns True or False.
    def test_isOverlap1(self):
        time = CourseTime.objects.create(start="09:00", end="11:00", day="M")
        time2 = CourseTime.objects.create(start="10:00", end="12:00", day="M")
        self.assertTrue(time.day == time2.day)
        self.assertTrue(time.start <= time2.start <= time.end)
        self.assertTrue(time2.start <= time.end <= time2.end)

    # Returns True or False.
    def test_isOverlap2(self):
        time = CourseTime.objects.create(start="09:00", end="11:00", day="M")
        time2 = CourseTime.objects.create(start="23:00", day="W")
        self.assertTrue(time.day != time2.day)
        self.assertFalse(time.start <= time2.start <= time.end)

    def test_User_login1(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertEquals(boyland.password, "unbreakable")

    def test_User_login2(self):
        User.objects.create(email="boyland@uwm.edu", password="unbreakable")
        boyland = User.objects.get(email="boyland@uwm.edu")
        self.assertNotEqual(boyland.password, "InvalidPasswordException")

    # def test_User_logout1(self):
    #     User.objects.create(email="boyland@uwm.edu", password="unbreakable")
    #     boyland = User.objects.get(email="boyland@uwm.edu")
    #     boyland.Login("unbreakable")
    #     self.assertEqual(boyland.Logout(), True)

    # def test_User_logout(self):
    #     User.objects.create(email="boyland@uwm.edu", password="unbreakable")
    #     boyland = User.objects.get(email="boyland@uwm.edu")
    #     self.assertEqual(boyland.Logout(), False)

    # def test_admin_classList1(self):
    #     x = User.objects.create(email="boyland@uwm.edu", password="unbreakable")
    #     Profile.objects.create(user=x, role=3)
    #     boyland = User.objects.get(email="boyland@uwm.edu")
    #     profile = Profile.objects.get(user=x)
    #

    def test1_assign(self):
        c1 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Boyland")
        c1.instructor = "Rock"
        c1.save()
        self.assertEqual(CourseTime.objects.get(number="351").instructor, "Rock")

    def test2_assign(self):
        c1 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Rock")
        c1.instructor = "Boyland"
        c1.save()
        self.assertNotEqual(CourseTime.objects.get(number="351").instructor, "Rock")

    def test3_assign(self):
        c2 = CourseTime.objects.create(department="CS", number="395", section="001", instructor="")
        c2.instructor = "Cheng"
        c2.save()
        self.assertEqual(CourseTime.objects.get(number="395").instructor, "Cheng")
        c2 = CourseTime.objects.create(department="CS", number="351", section="603", instructor="Rock")
        c2.instructor = ""
        c2.save()
        self.assertEqual(CourseTime.objects.get(number="351").instructor, "")


if __name__ == '__main__':
    unittest.main()
