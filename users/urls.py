from django.urls.conf import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.login, name='login'),
]