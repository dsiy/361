from django.test import TestCase
from CS361WebApp.models import Account, Administrator, TA, Instructor, InputManager, CourseTime

app = InputManager()


class AcceptanceTests(TestCase):
    # 1 admin login
    def test_isAdmin(self):
        # given a person logs in with admin account, i.e. boyland.uwm.edu
        # if not boyland's account, will return false
        Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        Account.objects.create(email="dssiy@uwm.edu", password="P4ssw0rd!")
        a = "login boyland.uwm.edu password Unbr3akable!"
        b = "login other.uwm.edu password P4ssw0rd!"
        self.assertEqual(app.command(a), "true")
        self.assertEqual(app.command(b), "false")

    def test_permissions(self):
        # have a list of permissions that are switched off.
        # if user is admin, then turn on permissions
        Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        Account.objects.create(email="dssiy@uwm.edu", password="P4ssw0rd!")
        a = "login boyland@uwm.edu Unbr3akable!"
        b = "login other@uwm.edu P4ssw0rd!"
        self.assertEqual(app.command(a), "true")
        self.assertEqual(app.command(b), "false")

    def test_commands(self):
        # given the permissions of the user, the user will show list of commands.
        # if user is admin, show full list. If not, show restricted list
        Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        Account.objects.create(email="dssiy@uwm.edu", password="P4ssw0rd!")
        a = "permission admin"
        b = "permission user"
        self.assertEqual(app.command(a), "Full List")
        self.assertEqual(app.command(b), "Restricted List")

    # 1 Admin login(Updated)
    def test_Login(self):
        # user will type in the command "Login" and they will be prompted with the following line of text:
        # Login
        # Enter Username:
        # Enter Password:
        Account.objects.create(email="hojin@uwm.edu", password="haha")
        a = "login hojin@uwm.edu haha"
        self.assertEqual(app.command(a), "Log-in Success!")
        # Not sure if this is the correct format for assertion test but I think this is what we should be checking

    # 2 Admin login failure
    def test_Login(self):
        # user will type in the command "Login" when they don't have an account
        # Login
        # Enter Username:
        # Enter Password:
        a = "login hojin@uwm.edu haha"
        self.assertEqual(app.command(a), "No Such User Exists!")

    # 3 Admin login failure
    def test_Login(self):
        # user will type in the command "Login"
        # Login
        # Enter Username:
        # Enter Password:
        # Enter login again when they are already logged in
        Account.objects.create(email="hojin@uwm.edu", password="haha")
        a = "login hojin@uwm.edu haha"
        self.assertEqual(app.command(a), "Log-in Success!")
        self.assertEqual(app.command(a), "You are already logged in!")

    # 2 Admin login failure
    def test_Login(self):
        # user will type in the command "Login"
        # Login
        # Enter Username:
        # Enter Incorrect Password:
        Account.objects.create(email="hojin@uwm.edu", password="haha")
        a = "login hojin@uwm.edu yeet"
        self.assertEqual(app.command(a), "Your password is incorrect!")

    # 2 User Log Out
    def test_logOut(self):
        # Test 1
        # Given that the user (TAs, Administrator, Instructor) presses the logout button
        # If the button is clicked then the user is redirected to the login screen.
        Account.objects.create(email="hojin@uwm.edu", password="haha")
        a = "login hojin@uwm.edu haha"
        self.assertEqual(app.command(a), "Log-in Success!")
        a = "logout"
        self.assertEqual(app.command(a), "Log-out Success!")

    # 3 Class list
    def test_isEmpty(self):
        # Test 1
        # When the admin passes in a command to view the class list
        # Class List is empty
        classes = CourseTime.object.create(classlist)
        a = classes.viewList()
        self.assertEqual(app.command(a), "Class List is Empty")

    def test2_isEmpty(self):
        # Test 2
        # When the class list isn't empty and the admin passes in a command to view the class list
        # ClassList = [{Class1, Section1, Hours1, Days1, Instructor1},...]
        b = Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        b.addClass("[{CS361, 800, 1100, T, Rock}]")
        classes = CourseTime.object.create(classlist)
        a = classes.viewList()
        self.assertEqual(app.command(a), "[{Class1, Section1, Hours1, Days1, Instructor1},...]")

    def test_search_class(self):
        # Test 3
        # When the admin enters the command to search the class list for a specific class via the class name and section number
        b = Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        b.addClass("[{CS361, 800, 1100, T, Rock}]")
        classes = CourseTime.object.create(classlist)
        a = classes.search("CS361, 800")
        self.assertEqual(app.command(a), "[{Class1, Section1, Hours1, Days1, Instructor1}]")

    def test_add_class(self):
        # Test 4
        # When the admin enters the command to add a class to the class list
        # Note: Class item details like hours, section, etc, will be asked step by step after class name is entered
        # Displayed differently here for convenience and clarity
        b = Administrator.objects.create(email="boyland.uwm.edu", password="Unbr3akable!")
        a = b.addClass("AddClass [{Class1, Section1, Hours1, Days1, Instructor1}]")
        self.assertEqual(app.command(a), "Class Successfully Added!")

    def test_remove_class(self):
        # Test 5
        # When the admin enters the class they want to remove from the class list by including thre class name and section number
        a = "Remove Class 'ClassName, Section' "
        self.assertEqual(app.command(a), "Class Successfully Removed")

    # 4 TA Account creation
    # setup account database
    # When admin creates an account
    def test_createTA(self):
        # Test 1
        # setup empty database
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        self.assertEqual(app.command(a), "TA account created")

    def test_createAccountUnique(self):
        # Test 2
        # setup with just boyland admin account
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        self.assertFalse(app.command(a))

    def test_validEmail(self):
        # Test 3
        a = TA.objects.create(email="yeetster@yeetyeet.org", password="notapassword")
        self.assertFalse(app.command(a))

    # 5 Administrator New Password Email
    # When the admin selects the command to send an email with a specific Password
    def test_sendEmail(self):
        # Test 1
        # The admin sends a command to send the new password to the TA via Email
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        t = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        b = a.resetPassword(t)
        self.assertEqual(app.command(b), "TA Password reset email sent")

    def test_newPasswordEmail(self):
        # Test 2
        # The TA resets their password Successfully
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        t = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        b = a.resetPassword(t)
        self.assertEqual(app.command(b), "Email with new password has been sent to your email")

    # 6 Administrator - Reset User Password

    # When the admin enters the command to reset a users password
    # Test 1
    def test_resetPasswordError(self):
        # If the admin selects a username that does not exist an error message will display
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        t = "fakeemail@uwm.edu"
        b = a.resetPassword(t)
        self.assertEqual(app.command(b), "Error Username <User Name> not found")

    def test_resetPasswordSuccsess(self):
        # Test 2
        # If the admin selects a username that exists to reset their password then the password will be set to a new random password and an email will be sent
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        t = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        b = a.resetPassword(t)
        self.assertEqual(app.command(a), "<Username> has been sent a new password successfully")

    # 7 TA User info
    def test_Name(self):
        # Test 1
        # When the user puts in a valid name, the information will be stored into the database.
        t = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        a = t.fill_Info(name="test")
        self.assertEqual(app.command(a), "Name successfully added.")

    def test_Password(self):
        # Test 2
        # When the user enters a valid password (1+ upper case, one number, 1+ symbol, 8+ characters), the information will be stored into the database
        t = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        a = t.fill_Info(name="test", password="Newp4ss!")
        self.assertEqual(app.command(a), "Password successfully added.")

    # 8 Password Reset System
    # User will get a temporary password when account is created, and can change password on first login.
    # Any further password resets handled by administrator.
    def test_send_tempPW(self):
        # Test 1
        # Send temporary password to new user via email
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        self.assertEqual(app.command(a), "Temporary Password is successfully sent to your email")

    def test_block_user(self):
        # Test 2
        # If user inputs their password 10 times block them out and display message to contact admin
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        x = a.Login(password='wrong') #should be 10 times?
        self.assertEqual(app.command(x), "You are blocked from the system. Contact Administrator")

    def test_email_admin(self):
        # Test 3
        # Send admin an email to reset the password
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        x = a.sendResetEmail()
        self.assertEqual(app.command(x), "Successfully Sent email to Administrator")

        # 9 Fill Out Schedule
        # The TA will fill out their own class schedule through the program.

    def test_check_valid_schedule(self):
        # Test 1
        # Ask user to input class name, time, and date of the class
        a = "Valid Class name, Time, and Date"
        self.assertEqual(app.command(a), "Valid schedule")

    def test_save_schedule(self):
        # Test 2
        # Save values to back-end with user key
        a = "TA Schedule"
        self.assertEqual(app.command(a), "Successfully Added")

        # 10 Validation of TA class choices

    def test_TA_schedule_and_selected_classes(self):
        # read through users schedule and if users schedule has a conflict with the selected class display message to user
        # Test 1
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        x = a.selectClasses()
        self.assertFalse(app.command(x), "Error class selected has a conflict with the schedule of the user")

        # 11 Backend - Priority System

    def test_priority_system(self):
        # Backend should implement priority system for scheduling of TA's.
        # TA will select a list of classes with the top being highest priority. Program will compare all TA's priority lists and create list with TA's assigned to classes based on priority
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        x = a.selectClasses()
        self.assertEqual(app.command(x), "<List of classes in priority order>")

    def test_priority_change(self):
        # Given a list of classes in priority order, TA will have the option to change their priority list. Program will reassign courses and display new priority list.
        a = TA.objects.create(email="testemail@yahoo.com", password="Test34!")
        x = a.selectClasses()
        self.assertEqual(app.command(x), "<Modified list of classes in priority order>")

        # 12 Instructor - Class view

    def test_View_Class1(self):
        # Test 1
        # Given instructor status, the user has permission to view the TAs in their class.
        a = Instructor.objects.create(email="rock@uwm.edu", password="R0ckr0ck$")
        b = a.viewTAs()
        self.assertTrue(app.command(a), "<Instructor>")
        self.assertEqual(app.command(b), "<List of TAs in Classname>")

    # 13 Administrator - Assigning Instructors to Courses
    def test_Assign_Courses1(self):
        # Test 1
        # Given the user is an administrator, the has permission to assign TAs to courses
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        self.assertTrue(app.command(a), "<Administrator>")

    def test_Assign_Courses2(self):
        # Test 2
        # Given administrative access, the user can assign TAs to assign courses.
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        x = a.assignTA()
        self.assertTrue(app.command(x), "TA assigned.")

    # Tests for viewing the class list

    def test_view_classlist1(self):
        # Test 1
        # Given administrative access, the user can assign TAs to assign courses.
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        x = a.viewClassList()
        self.assertEqual(app.command(x), "Class List is Empty")

    def test_view_classlist2(self):
        # Test 2
        # Given administrative access, the user can assign TAs to assign courses.
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        c1 = "CS361 802 1400 1600 Tuesday Rock"
        c2 = "CS395 801 1200 1300 Monday Cheng"
        ac1 = a.addClass(c1)
        self.assertEqual(app.command(ac1), "Class Successfully Added!")
        ac2 = a.addClass(c2)
        self.assertEqual(app.command(ac2), "Class Successfully Added!")
        x = a.viewClassList()
        self.assertEqual(app.command(x), "CS361 802 1400 1600 Rock\nCS395 801 1200 1300 Cheng\n")

    def test_view_classlist3(self):
        # Test 3
        # Given administrative access, the user can assign TAs to assign courses.
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        c1 = "CS361 802 1400 1600 Tuesday Rock"
        c2 = "CS395 801 1200 1300 Monday Cheng"
        c3 = "CS395 801 1200 1300"
        ac1 = a.addClass(c1)
        self.assertEqual(app.command(ac1), "Class Successfully Added!")
        ac2 = a.addClass(c2)
        self.assertEqual(app.command(ac2), "Class Successfully Added!")
        ac3 = a.addClass(c3)
        self.assertEqual(app.command(ac2), "Class is missing information and was not added!")
        x = a.viewClassList()
        self.assertEqual(app.command(x), "CS361 802 1400 1600 Rock\nCS395 801 1200 1300 Cheng\n")

    def test_view_classlist3(self):
        # Test 3
        # Given administrative access, the user can assign TAs to assign courses.
        a = Administrator.objects.create(email="boyland@uwm.edu", password="Unbr3akable!")
        c1 = "CS361 802 1400 1600 Tuesday Rock"
        c2 = "CS395 801 1200 1300 Monday Cheng"
        c3 = "CS395 801 1200 1300 Monday Cheng"
        ac1 = a.addClass(c1)
        self.assertEqual(app.command(ac1), "Class Successfully Added!")
        ac2 = a.addClass(c2)
        self.assertEqual(app.command(ac2), "Class Successfully Added!")
        ac3 = a.addClass(c3)
        self.assertEqual(app.command(ac2), "Class already exists and was not added!")
        x = a.viewClassList()
        self.assertEqual(app.command(x), "CS361 802 1400 1600 Rock\nCS395 801 1200 1300 Cheng\n")