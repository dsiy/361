from django.test import TestCase
import unittest
from CS361WebApp.models import User, CourseTime, CreatePriority, SavePriority
from CS361WebApp.validator import validate_alpha, validate_numeric


class TATestCase(TestCase):

    def test_TA_priority_create1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=1)
        b = CreatePriority.objects.create(classes=y, priority=2)
        c = CreatePriority.objects.create(classes=z, priority=3)
        alist = [a, b, c]
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        priority = 0
        for classes in profile.myList.all():
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_TA_priority_create2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=2)
        b = CreatePriority.objects.create(classes=y, priority=3)
        c = CreatePriority.objects.create(classes=z, priority=1)
        alist = [c, a, b]
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        profile = SavePriority.objects.filter(user=santha)
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        priority = 0
        for classes in x:
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_TA_priority_create3(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=1)
        b = CreatePriority.objects.create(classes=y, priority=2)
        c = CreatePriority.objects.create(classes=z, priority=3)
        c.priority = 1
        a.priority = 2
        b.priority = 3
        a.save()
        b.save()
        c.save()
        alist = [c, a, b]
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        profile = SavePriority.objects.filter(user=santha)
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        priority = 0
        for classes in x:
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_TA_priority_view_empty(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        profile = SavePriority.objects.create(user=santha)
        count = 0
        for classes in profile.myList.all():
            count += 1
        self.assertEquals(count, 0)

    def test_TA_priority_overlap(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        list = ["CS395", "CS337", "CS361"]
        self.assertEqual(santha.addClass("CS361", 1), True)
        self.assertEqual(santha.addClass("CS337", 1), True)
        self.assertEqual(santha.addClass("CS395", 1), True)
        self.assertEqual(santha.viewPriority(), "CS395")

    def test_TA_priority_remove1(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=1)
        b = CreatePriority.objects.create(classes=y, priority=2)
        c = CreatePriority.objects.create(classes=z, priority=3)
        alist = [a, b]
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        profile.myList.remove(c)
        profile = SavePriority.objects.filter(user=santha)
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        priority = 0
        for classes in x:
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_TA_priority_remove2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=1)
        b = CreatePriority.objects.create(classes=y, priority=2)
        c = CreatePriority.objects.create(classes=z, priority=3)
        alist = [a]
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        profile.myList.remove(c)
        profile.myList.remove(b)
        profile = SavePriority.objects.filter(user=santha)
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        priority = 0
        for classes in x:
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_TA_priority_remove3(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        x = CourseTime.objects.create(department="CS", number="361")
        y = CourseTime.objects.create(department="CS", number="337")
        z = CourseTime.objects.create(department="CS", number="395")
        a = CreatePriority.objects.create(classes=x, priority=1)
        b = CreatePriority.objects.create(classes=y, priority=2)
        c = CreatePriority.objects.create(classes=z, priority=3)
        alist = []
        profile = SavePriority.objects.create(user=santha)
        profile.myList.add(a)
        profile.myList.add(b)
        profile.myList.add(c)
        profile.myList.remove(c)
        profile.myList.remove(b)
        profile.myList.remove(a)
        profile = SavePriority.objects.filter(user=santha)
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        priority = 0
        for classes in x:
            self.assertEqual(classes, alist[priority])
            priority += 1

    def test_create_priority1(self):
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.get(classes=c361), c1)

    def test_create_priority2(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        self.assertEquals(CreatePriority.objects.filter(classes=c395).first(), None)

    def test_create_priority3(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="3")
        self.assertEquals(CreatePriority.objects.get(priority="3"), c2)

    def test_create_priority4(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertEquals(CreatePriority.objects.filter(priority="1").first, c2)

    def test_create_priority5(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="1")
        self.assertNotEquals(CreatePriority.objects.filter(priority="1").first(), c1)

    def test_create_priority6(self):
        User.objects.create(email="skravi@uwm.edu", password="imaTA32!")
        santha = User.objects.get(email="skravi@uwm.edu")
        c361 = CourseTime.objects.create(department="CS", number="361", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c395 = CourseTime.objects.create(department="CS", number="395", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c458 = CourseTime.objects.create(department="CS", number="458", start="11:00", end="11:50", day="TTH",
                                         section="802", instructor="Rock")
        c1 = CreatePriority.objects.create(classes=c361, priority="1")
        c2 = CreatePriority.objects.create(classes=c458, priority="2")
        self.assertNotEquals(CreatePriority.objects.filter(priority="2").first(), None)

    # Tests for validating strings and numeric values

    def test_acceptance_validator1(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha("2")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator2(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha("%")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator3(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha("3:")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator4(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha("hell0")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator5(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha("!nop3")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator6(self):
        # validate alphabetic
        with self.assertRaises(ValidationError) as cm:
            validate_alpha(" ")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must not contain numbers or symbols')

    def test_acceptance_validator7(self):
        # validate number
        with self.assertRaises(ValidationError) as cm:
            validate_numeric("")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must be comprised only of numbers')

    def test_acceptance_validator8(self):
        # validate number
        with self.assertRaises(ValidationError) as cm:
            validate_numeric("678h")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must be comprised only of numbers')

    def test_acceptance_validator9(self):
        # validate number
        with self.assertRaises(ValidationError) as cm:
            validate_numeric("6%")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must be comprised only of numbers')

    def test_acceptance_validator10(self):
        # validate number
        with self.assertRaises(ValidationError) as cm:
            validate_numeric("  6")
        the_exception = cm.exception
        self.assertEqual(the_exception.message, 'data must be comprised only of numbers')


class InstructorTestCase(TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
