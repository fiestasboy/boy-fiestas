from django.urls.conf import path, include
from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout_user', views.logout_user, name='logout_user'),
]