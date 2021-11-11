from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, CustomAuthForm




def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Account succesfully created. You can now login')
            return redirect('accounts:login')
    return render(request, "accounts/register.html", context = {"form":form})

def login_user(request):
    form = CustomAuthForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email = cd['email'], password=cd['password']) 
            if user is not None:
                login(request, user)
                return redirect(request.GET.get('next','accounts:dashboard'))
            else:
                messages.error(request, 'Account does not exist')
    return render(request, "accounts/login.html", context = {"form":form})

@login_required
def logout_user(request):
    logout(request)
    return redirect("accounts:login")


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

