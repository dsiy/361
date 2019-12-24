from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UpdateInformationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import Profile


def admin_check(user):
    return user.is_staff


@login_required
def updateinfo(request):
    if request.method == 'POST':
        form = UpdateInformationForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            person = Profile.objects.get(user=request.user)
            person.firstname = form.cleaned_data.get('firstname')
            person.lastname = form.cleaned_data.get('lastname')
            person.address = form.cleaned_data.get('address')
            person.phone = form.cleaned_data.get('phone')
            person.save()

            messages.success(request, f'information updated for {request.user}!')
            return redirect('CS361WebApp-updateinfo')
    else:
        form = UpdateInformationForm()

    return render(request, 'user/UpdateInfo.html', {'form': form})


@login_required
@user_passes_test(admin_check)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            person = Profile.objects.get(user__username=form.cleaned_data.get('username'))
            person.role = form.cleaned_data.get('role')
            person.save()

            messages.success(request, f'Account created for {username}')
            return redirect('CS361WebApp-home')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

# def login(request):
#     form = UserRegisterForm()
#     return render(request, 'user/login.html', {'form': form})
