import operator
from functools import reduce

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from CS361WebApp.models import CourseTime, SavePriority, CreatePriority
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm, AssignUserForm, Priority
from user.models import Profile


def admin_check(user):
    return user.is_staff


@login_required
def home(request):
    course_result = CourseTime.objects.all()
    profile = Profile.objects.filter(user=request.user)

    return render(request, 'CS361WebApp/home.html', {"courses": course_result, 'profile': profile})


@login_required
@user_passes_test(admin_check)
def coursetime(request):
    if request.method == 'POST':
        form = CourseTimeForm(request.POST)
        # need to put is_valid here
        if form.is_valid():
            form.save()
            department = form.cleaned_data.get('department')
            number = form.cleaned_data.get('number')

            messages.success(request, f'Course created for {department} {number}!')
            return redirect('CS361WebApp-coursetime')

    else:
        form = CourseTimeForm()
    return render(request, 'CS361WebApp/CourseTime.html', {'form': form})


@login_required
def assign(request):
    form = AssignUserForm(request.POST)
    person = Profile.objects.get(user=request.user)
    if person.role == 1:
        return redirect('CS361WebApp-home')
    if form.is_valid():
        class1 = form.cleaned_data.get('course')
        instructor = form.cleaned_data.get('instructor')
        if person.role == 2 and instructor.role == 2:
            return redirect('CS361WebApp-assign')
        class1.instructor = str(instructor)
        section = int(class1.section)
        if instructor.role == 1:
            if section < 401:
                class1.instructor = ''
        elif instructor.role == 2:
            if section > 401:
                class1.instructor = ''
        class1.save()
        messages.success(request, f'{instructor} assigned to {class1}!')
        redirect('CS361WebApp-home')
    return render(request, 'CS361WebApp/assign.html', {'form': form})


@login_required
def classlist(request):
    classes = CourseTime.objects.all()
    profile = SavePriority.objects.filter(user=request.user)
    x = profile.all()
    for yeet in profile:
        x = yeet.myList.order_by('priority')
    if request.method == 'POST':
        form = Priority(request.POST)

        if form.is_valid():

            name = request.user
            found = SavePriority.objects.filter(user=name).first()
            if found is None:
                useradd = SavePriority.objects.create(user=name)
            else:
                useradd = SavePriority.objects.filter(user=name).first()
            form.save()
            course = form.cleaned_data.get('classes')
            priority = form.cleaned_data.get('priority')

            add = CreatePriority.objects.filter(classes=course).filter(priority=priority).first()
            test = SavePriority.objects.filter(user=name)

            changed1 = 121111105110107
            changed2 = 121101101116
            for yeeet in test:
                x = yeeet.myList.all()
                for yeet in x:
                    if int(yeet.priority) == priority:
                        changed1 = 69  # fuck
                        joe_mama = yeet
                    if yeet.classes == course:
                        changed2 = 420
                        i_hate_my_life = yeet
            if changed1 == 69 and changed2 == 420:
                useradd.myList.remove(joe_mama)
                useradd.myList.remove(i_hate_my_life)
                useradd.myList.add(add)
                messages.error(request, f'Class replaced!')
            elif changed1 == 69:
                useradd.myList.remove(joe_mama)
                useradd.myList.add(add)
                messages.error(request, f'Class replaced!')
            elif changed2 == 420:
                useradd.myList.remove(i_hate_my_life)
                useradd.myList.add(add)
                messages.error(request, f'Class replaced!')
            else:
                useradd.myList.add(add)
                messages.success(request, f'{course} assigned to {name} with priority {priority}!')

        profile = SavePriority.objects.filter(user=request.user)
        x = profile.all()
        for yeet in profile:
            x = yeet.myList.order_by('priority')
        return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'x': x, 'form': form})
    else:

        form = Priority(request.POST)
    return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'x': x, 'form': form})


def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
