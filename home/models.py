from django.db import models
from datetime import datetime

class Treino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    peso = models.IntegerField()
    repeticao = models.IntegerField()
    
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
