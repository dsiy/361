from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from CS361WebApp.models import CourseTime, PriorityList, Profile
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm, AssignUserForm, PriorityForm
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
        form = PriorityForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            number = form.cleaned_data.get('number')
            section = form.cleaned_data.get('section')
            priority = form.cleaned_data.get('priority')

            class1 = classes.filter(department=department).filter(number=number).filter(section=section)
            if class1.count() == 0:
                messages.error(request, f'Class not found!')
                return redirect('CS361WebApp-classList')

            currentuser = request.user
            currentuser.prior_class = class1
            currentuser.save()

            return redirect('CS361WebApp-classList')
    else:
        form = PriorityForm()
    return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})


def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
