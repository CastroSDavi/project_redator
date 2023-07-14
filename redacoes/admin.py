from django.contrib import admin
from .models import Temas, Categoria
# Register your models here.
class TemasAdmin(admin.ModelAdmin):
    list_display = ['tema', 'mostrar']
    list_editable = ['mostrar']
    list_per_page = 10
    list_max_show_all = 100
    
class CategoriaAdmin(admin.ModelAdmin):
    list_per_page = 10
    

admin.site.register(Temas, TemasAdmin)
admin.site.register(Categoria, CategoriaAdmin)