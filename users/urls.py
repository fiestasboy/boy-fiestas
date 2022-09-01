from django.urls.conf import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
]