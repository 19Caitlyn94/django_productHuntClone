from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # User has info and wants to create an account
        # Check if passwords match, if not, return page including an error
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'username_error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else: return render(request, 'accounts/signup.html', {'password_error': 'Passwords do not match'})
    else:
        #user wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO Need to route to homepage
    # Dont forget to logout
    return render(request, 'accounts/signup.html')
