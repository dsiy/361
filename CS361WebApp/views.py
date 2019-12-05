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
    form = AssignUserForm()
    return render(request, 'CS361WebApp/assign.html', {'form': form})


@login_required()
def classlist(request):
    classes = CourseTime.objects.all()
    if request.method == 'POST':
        form = PriorityForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data.get('department')
            number = form.cleaned_data.get('number')
            section = form.cleaned_data.get('section')
            priority = form.cleaned_data.get('priority')
            myModel = SavePriority()
            class1 = classes.filter(department=department).filter(number=number).filter(section=section)
            num = class1.count()
            if num == 0:
                messages.error(request, f'Class not found!')
                return redirect('CS361WebApp-classList')
            myModel.myList.append(class1)
            # myJsonList = json.dumps(myModel.myList)
            # jsonDec = json.decoder.JSONDecoder()
            # string = str(jsonDec.decode(myJsonList))
            # listIWantToStore = str(jsonDec.decode(myJsonList))[1:-1].split(',')
            #
            # listIWantToStore.append(class1.get(number=number).__str__())
            # myModel.myList = json.dumps(listIWantToStore)
            myModel.save()
        return redirect('CS361WebApp-classList')
    else:
        form = PriorityForm()
    return render(request, 'CS361WebApp/ClassList.html', {'classes': classes, 'form': form})


def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
