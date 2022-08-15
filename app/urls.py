from django.urls import include
from django.urls.conf import path


from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/accounts/', include('allauth.urls')),
    path('login', views.login, name='login'),
   
]