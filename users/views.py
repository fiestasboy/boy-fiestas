from django.shortcuts import render


def login(resquest):
    return render(resquest, 'login.html')
