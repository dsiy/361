from django.shortcuts import render
from django.views import View
from django.contrib import auth
from django.http import HttpResponseRedirect
from .forms import LoginForm
from CS361WebApp.models import InputManager


class TAManager(View):
    def get(self, request):
        return render(request, 'main/index.html')

    def post(self, request):
        manager = InputManager()
        commandInput = request.POST["command"]
        if commandInput:
            response = manager.command(commandInput)
        else:
            response = ""
        return render(request, 'main/index.html', {"message": response})

class Welcome(View):
    def get(self, request):
        return render(request, "main/welcome.html", {'form': LoginForm})

    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin/')
        else:
            return HttpResponseRedirect('/accounts/invalid/')