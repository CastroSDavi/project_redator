from django.urls import path
from . import views

urlpatterns:list = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]