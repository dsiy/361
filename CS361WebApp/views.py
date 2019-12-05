import operator
from functools import reduce

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from CS361WebApp.models import CourseTime, SavePriority
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm, AssignUserForm
from CS361WebApp.forms import CourseTimeForm, PriorityInit
import json


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

        messages.success(request, f'Account created for {number}!')
        return redirect('CS361WebApp-coursetime')

    else:
        form = CourseTimeForm()
    return render(request, 'CS361WebApp/CourseTime.html', {'form': form})


@login_required()
def assign(request):
    form = AssignUserForm()
    return render(request, 'CS361WebApp/assign.html', {'form': form})


@login_required()
def classlist(request):
    classes = CourseTime.objects.all()
    if request.method == 'POST':
        form = PriorityInit(request.POST)
        if form.is_valid():
            form.save()
            department = form.cleaned_data.get('department')
            number = form.cleaned_data.get('number')
            section = form.cleaned_data.get('section')
            priority = form.cleaned_data.get('priority')
            myModel = SavePriority()
            class1 = classes.filter(department=department).filter(number=number).filter(section=section)
            num = class1.count()
            if num == 0:
                messages.error(request, f'Class not found!')
                SavePriority.objects.filter(department=department).filter(number=number).filter(section=section).delete()
                return redirect('CS361WebApp-classList')
            # myModel.myList.insert(int(priority), class1)
            messages.success(request, f'{number} added as priority {priority}!')
        # return redirect('CS361WebApp-classList')
        form = PriorityInit()
        return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})
    else:
        form = PriorityInit()

    return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})


def priority(request):
    classes = SavePriority.objects.all()
    if request.method == 'POST':
        return redirect('CS361WebApp-priority')
    return render(request, "CS361WebApp/priority.html", {'classes': classes})


def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
