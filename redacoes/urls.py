from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temas', views.temas, name='temas'),
    path('temas/create', views.create, name='create'),
    path('temas/search', views.search_temas, name='search_temas')
]