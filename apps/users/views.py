from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):
    return render(request, "users/login.html")
 
def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Nombre de usuario ya está en uso')
            return redirect('/login')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Correo ya está en uso')
            return redirect('/login')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('/')
    else:
        return render(request, 'login.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Nombre de usuario o contraseña inválido')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')