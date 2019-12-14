import operator
from functools import reduce

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from CS361WebApp.models import CourseTime, SavePriority, CreatePriority
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm, AssignUserForm, PriorityList, Priority
# from CS361WebApp.forms import CourseTimeForm, PriorityInit
import json
from typing import Any


def admin_check(user):
    return user.is_staff


@login_required
def home(request):
    course_result = CourseTime.objects.all()
    return render(request, 'CS361WebApp/home.html', {"courses": course_result})


@login_required
@user_passes_test(admin_check)
def coursetime(request):
    if request.method == 'POST':
        form = CourseTimeForm(request.POST)
        # need to put is_valid here
        form.save()

        department = form.cleaned_data.get('department')
        number = form.cleaned_data.get('number')
        start = form.cleaned_data.get('start')
        end = form.cleaned_data.get('end')
        day = form.cleaned_data.get('day')
        section = form.cleaned_data.get('section')
        instructor = form.cleaned_data.get('instructor')

        messages.success(request, f'Course created for {department} {number}!')
        return redirect('CS361WebApp-coursetime')

    else:
        form = CourseTimeForm()
    return render(request, 'CS361WebApp/CourseTime.html', {'form': form})


@login_required
def assign(request):
    classes = CourseTime.objects.all()
    form = AssignUserForm(request.POST)
    if form.is_valid():
        department = form.cleaned_data.get('department')
        number = form.cleaned_data.get('number')
        section = form.cleaned_data.get('section')
        instructor = form.cleaned_data.get('instructor')
        class1 = classes.filter(department=department).filter(number=number).filter(section=section)
        num = class1.count()
        if num == 0:
            messages.error(request, f'Class not found!')
            return redirect('CS361WebApp-classList')
        class1.update(instructor=instructor)
        messages.success(request, f'{instructor} assigned to {department} {number} {section}!')
    return render(request, 'CS361WebApp/assign.html', {'form': form})


@login_required
def classlist(request):
    classes = CourseTime.objects.all()
    if request.method == 'POST':
        form = Priority(request.POST)

        if form.is_valid():
            tas = SavePriority.objects.all()
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
            useradd.myList.add(add)
            messages.success(request, f'{course} assigned to {name} with priority {priority}!')
        return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})
    else:

        form = Priority(request.POST)
    return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})


@login_required()
def priority(request):
    profile = SavePriority.objects.filter(user=request.user)
    if request.method == 'POST':
        return redirect('CS361WebApp-priority')
    return render(request, "CS361WebApp/priority.html", {'classes': profile})

@login_required()
def dashboard(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/dashboard.html")
