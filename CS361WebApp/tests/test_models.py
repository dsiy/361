from django.test import TestCase
import unittest
from CS361WebApp.models import User, CourseTime, CreatePriority, SavePriority
from CS361WebApp.validator import validate_alpha, validate_numeric
from django.core.exceptions import ValidationError

class TATestCase(TestCase):

    def test_TA_priority_create1(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_create2(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "cS337", "CS395"]
        self.assertEqual(santha.addClass("cs361", 1), True)
        self.assertEqual(santha.addClass("cS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_create3(self):
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
        santha = User.objects.get(email="skravi@uwm.edu")
        list = []
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view1(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["cs361", "CS337", "CS395"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 3), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_view2(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 2), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), ["CS395", "CS37"])

    def test_TA_priority_overlap(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), "CS395")

    def test_TA_priority_remove1(self):
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
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS361", "CS395", "CS337"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS395", 3), True)
        self.assertEqual(santha.changePriority("CS337", 2), True)
        self.assertEqual(santha.changePriority("CS361", 1), True)
        self.assertEqual(santha.viewPriority(), list)

    def test_TA_priority_change2(self):
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.changePriority("CS361", 1), False)
        self.assertEqual(santha.changePriority("CS337", 1), False)
        self.assertEqual(santha.changePriority("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), ["CS395"])

    def test_create_priority1(self):
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.get(classes=c361), c1)

    def test_create_priority2(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.get(classes=c395), None)

    def test_create_priority3(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="3")
        self.assertEquals(CreatePriority.objects.get(priority="3"), c2)

    def test_create_priority4(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertEquals(CreatePriority.objects.get(priority="1"), c2)

    def test_create_priority5(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertNotEquals(CreatePriority.objects.get(priority="1"), c1)

    def test_create_priority5(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="one")
        self.assertNotEquals(CreatePriority.objects.get(priority="one"), None)

    def test_save_priority1(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        c361 = CourseTime.objects.create(department="CS", number="361", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="1100", end="1150", day="TTH", section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="3")
        pList = CreatePriority.objects.all()
        sp1 = SavePriority.objects.create(user=santha, myList=pList)
        self.assertEquals(SavePriority.objects.get(user=santha), sp1)

    def test_save_priority2(self):
        santha = User.objects.create_user("santha", "skravi@uwm.edu", "imaTA32!")
        bryan = User.objects.create_user("bryan", "stoffleb@uwm.edu", "iamTA55!")
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

    # Tests for validating strings and numeric values

    def test_alpha_validator1(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha('2')
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_alpha_validator2(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha('%')
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_alpha_validator3(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha('3')
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_alpha_validator4(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha('hello0')
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_alpha_validator5(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha("Zer0")
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_alpha_validator6(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as e:
            validate_alpha(' ')
        self.assertEqual(e.exception.message, 'data must not contain numbers or symbols')

    def test_numeric_validator1(self):
        # validate number
        with self.assertRaises(ValidationError) as e:
            validate_numeric('')
        self.assertEqual(e.exception.message, 'data must be comprised only of numbers')

    def test_numeric_validator2(self):
        # validate number
        with self.assertRaises(ValidationError) as e:
            validate_numeric('678h')
        self.assertEqual(e.exception.message, 'data must be comprised only of numbers')

    def test_numeric_validator3(self):
        # validate number
        with self.assertRaises(ValidationError) as e:
            validate_numeric('6%')
        self.assertEqual(e.exception.message, 'data must be comprised only of numbers')

    def test_numeric_validator4(self):
        # validate number
        with self.assertRaises(ValidationError) as e:
            validate_numeric(' 6')
        self.assertEqual(e.exception.message, 'data must be comprised only of numbers')

class InstructorTestCase(TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
