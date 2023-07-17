from django.shortcuts import render
from ..forms import RegisterForm
def register(request):
    
    form = RegisterForm()
    
    return render(request,'authentication/register.html')