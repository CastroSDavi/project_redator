from django.shortcuts import render, redirect
from ..models import Temas

def search_temas(request): 
    search_temas = request.GET.get('q','').strip()
    temas = Temas.objects.filter(tema__icontains=search_temas).order_by('-id')

    if search_temas == '':
        return redirect("/temas")
    
    context = {
        'search_temas':search_temas,
        'temas': temas
    }
    return render(request,'temas/temas.html', context)