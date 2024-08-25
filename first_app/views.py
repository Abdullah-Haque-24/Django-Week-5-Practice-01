from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account created successfully")
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid(): 
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name, password = userpass) 
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully")
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {"user" : request.user})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def pass_change(request):
    if request.method=='POST':
        pass_change_form = PasswordChangeForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.warning(request, "Password has been updated successfully!")
            update_session_auth_hash(request, pass_change_form.user) 
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user = request.user)
    return render(request, 'pass_change.html', {'form': pass_change_form})

def without_Old_pass_change(request):
    if request.method=='POST':
        pass_change_form = SetPasswordForm(request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.warning(request, "Password has been updated successfully!")
            update_session_auth_hash(request, pass_change_form.user) 
            return redirect('profile')
    else:
        pass_change_form = SetPasswordForm(user = request.user)
    return render(request, 'without_old_pass.html', {'form': pass_change_form})