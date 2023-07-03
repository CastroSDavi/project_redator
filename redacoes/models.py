from django.db import models

# Create your models here.
class Redacao(models.Model):
    tema = models.CharField(max_length=255)