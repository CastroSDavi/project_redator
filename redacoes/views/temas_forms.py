from django.shortcuts import render

def create(request):
    context = {}
    return render(request,'temas/create.html',context)