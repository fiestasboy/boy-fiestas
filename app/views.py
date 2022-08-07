from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def login(resquest):
    return render(resquest, 'login.html')

