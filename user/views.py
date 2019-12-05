from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required, user_passes_test


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
            messages.success(request, f'Account created for {username}!')
            return redirect('CS361WebApp-home')

    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

# def login(request):
#     form = UserRegisterForm()
#     return render(request, 'user/login.html', {'form': form})
