from re import template
from django.urls.conf import path, include
from . import views

app_name = 'users'

from django.views.generic import TemplateView

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='users/login.html'), name='login'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout_user', views.logout_user, name='logout_user'),
]