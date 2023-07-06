from django.shortcuts import render
from ..models import Redacao

def temas(request):
    redacoes = Redacao.objects.filter(mostrar=True)
    
    context = {
        'redacoes': redacoes
    }
    
    return render(request, 'redacoes/temas.html', context)