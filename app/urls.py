from django.urls.conf import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
]