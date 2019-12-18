from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate


def admin_check(user):
    return user.is_staff


@login_required
@user_passes_test(admin_check)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')
            if role == '1':
                request.user.user_permissions.name = 'TA'
                request.user.save()
                yeet = request.user.user_permissions.name
            messages.success(request, f'Account created for {username} with role {role}!')
            return redirect('CS361WebApp-home')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

# def login(request):
#     form = UserRegisterForm()
#     return render(request, 'user/login.html', {'form': form})
