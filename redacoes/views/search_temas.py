from django.shortcuts import render, redirect
from ..models import Redacao

def search_temas(request): 
    search_temas = request.GET.get('q','').strip()
    redacoes = Redacao.objects.filter(tema__icontains=search_temas)

    if search_temas == '':
        return redirect("/temas")
    
    context = {
        'search_temas':search_temas,
        'redacoes': redacoes
    }
    return render(request,'redacoes/temas.html', context)