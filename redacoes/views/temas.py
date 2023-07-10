from django.shortcuts import render
from ..models import Redacao, Categoria

def temas(request):
    ordenacao = request.GET.get('order_by','-id')
    filtro = request.GET.getlist('filter')
    
    redacoes = Redacao.objects.filter(categoria_id__in=filtro).order_by(ordenacao)
    
    categorias = Categoria.objects.all()
    if not ordenacao:
        ordenacao = '-id'
        
    if filtro:
        redacoes = Redacao.objects.filter(mostrar=True, categoria_id__in=filtro).order_by(ordenacao)
    
    if not filtro:
        redacoes = Redacao.objects.filter(mostrar=True).order_by(ordenacao)
        
    
    context = {
        'categorias': categorias,
        'redacoes': redacoes
    }
    
    return render(request, 'redacoes/temas.html', context)