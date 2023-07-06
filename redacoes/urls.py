from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('temas', views.temas, name='temas'),
    path('temas/search', views.search_temas, name='search_temas')

]