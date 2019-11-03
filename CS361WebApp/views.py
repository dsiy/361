from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

#this still needs to be integrated once we make a class to take input
class TAManager(View):
    def get(self, request):
        return render(request, 'main/index.html')

    def post(self, request):
        yourInstance = YourClass()
        commandInput = request.POST["command"]
        if commandInput:
            response = yourInstance.command(commandInput)
        else:
            response = ""
        return render(request, 'main/index.html', {"message": response})

#this works but is just test data, still needs call and response
def home(request):
    return render(request, "main/index.html")


def about(request):
    return render(request, "main/about.html")
