from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):
    return render(request, "login.html")
 
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken')
            return redirect('/users/sign_up')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already taken')
            return redirect('/users/sign_up')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('/users/sign_in')
    else:
        return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('users/sign_in')
    else:
        return render(request, 'sign_in.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')