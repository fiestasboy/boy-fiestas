from django.urls import include
from django.urls.conf import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/accounts/', include('allauth.urls')),
    path('login', views.login, name='login'),
]