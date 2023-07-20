from django.shortcuts import render
from ..forms import TemasForm

def create(request):    
    
    if request.method == 'POST':
        
        context = {
            'form': TemasForm(request.POST)
        }
        
        return render(request,'temas/create_temas.html',context)
    
    context = {
        'form': TemasForm()
    }
    
    return render(request,'temas/create_temas.html',context)