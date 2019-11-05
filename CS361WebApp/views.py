from django.shortcuts import render
from django.views import View
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

def about(request):
    return render(request, "main/about.html")
