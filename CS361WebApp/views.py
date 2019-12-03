from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from CS361WebApp.models import CourseTime
from django.contrib.auth.decorators import login_required, user_passes_test
from CS361WebApp.forms import CourseTimeForm

def admin_check(user):
    return user.is_staff

lists = {
        'CS361',
        'CS351',
        'CS458',
        }
@login_required
def home(request):
    # course_result = CourseTime.objects.all()
    course_result = lists
    return render(request, 'CS361WebApp/home.html', {"courses": course_result})

@login_required
@user_passes_test(admin_check)
def coursetime(request):
    if request.method == 'POST':
        form = CourseTimeForm(request.POST)

        department = form.cleaned_data.get('department')
        username = form.cleaned_data.get('username')
        username = form.cleaned_data.get('username')
        username = form.cleaned_data.get('username')
        username = form.cleaned_data.get('username')
        username = form.cleaned_data.get('username')

        messages.success(request, f'Account created for {username}!')
        return redirect('CS361WebApp-coursetime')

    else:
        form = CourseTimeForm()
    return render(request, 'CS361WebApp/CourseTime.html', {'form': form})


# def home(request):
#     manager = InputManager()
#     commandInput = request.POST["command"]
#     if commandInput:
#         response = manager.command(commandInput)
#     else:
#         response = ""
#     return render(request, 'CS361WebApp/home.html', {"message": response})

def welcome(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, "CS361WebApp/welcome.html")
