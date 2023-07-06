from django.contrib import admin
from .models import Redacao, Categoria
# Register your models here.
class RedacaoAdmin(admin.ModelAdmin):
    list_display = ['tema', 'mostrar']
    list_editable = ['mostrar']
    list_per_page = 10
    list_max_show_all = 100
    
class CategoriaAdmin(admin.ModelAdmin):
    list_per_page = 10
    

admin.site.register(Redacao, RedacaoAdmin)
admin.site.register(Categoria, CategoriaAdmin)