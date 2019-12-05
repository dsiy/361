from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages
from CS361WebApp.models import CourseTime, SavePriority
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm, AssignUserForm
from CS361WebApp.forms import CourseTimeForm, PriorityForm
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
    form = CourseTimeForm()
    return render(request, 'CS361WebApp/assign.html', {'form': form})


def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
