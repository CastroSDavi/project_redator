from django.shortcuts import render

def create(request):
    return render(request,'temas/create_temas.html')