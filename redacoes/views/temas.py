from django.shortcuts import render
from ..models import Temas, Categoria

def temas(request):
    ordenacao = request.GET.get('order_by','-id')
    filtro = request.GET.getlist('filter')
    
    temas = Temas.objects.filter(categoria_id__in=filtro).order_by(ordenacao)
    
    categorias = Categoria.objects.all()
    
    if not ordenacao:
        ordenacao = '-id'
        
    if filtro:
        temas = Temas.objects.filter(mostrar=True, categoria_id__in=filtro).order_by(ordenacao)
    
    if not filtro:
        temas = Temas.objects.filter(mostrar=True).order_by(ordenacao)
        
    context = {
        'categorias': categorias,
        'temas': temas
    }
    
    return render(request, 'temas/temas.html', context)