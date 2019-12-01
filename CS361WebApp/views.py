from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from CS361WebApp.models import InputManager
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def home(request):
    manager = InputManager()
    commandInput = request.POST
    if commandInput:
        response = manager.command(commandInput)
    else:
        response = ""
    return render(request, 'CS361WebApp/home.html', {"message": response})


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
