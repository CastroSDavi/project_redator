from django.db import models
# Create your models here.

class Categoria(models.Model):
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    nome = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nome
    
class Redacao(models.Model):
    class Meta:
        verbose_name = 'Redacao'
        verbose_name_plural= 'Redacoes'
        
    tema = models.CharField(max_length=255);
    imagem = models.ImageField(upload_to='pictures/%y/%m', blank=True)
    texto1 = models.TextField(blank=True);
    texto2 = models.TextField(blank=True);
    mostrar = models.BooleanField(default=True);
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True, 
        null=True
        )
    
    def __str__(self) -> str:
        return self.tema