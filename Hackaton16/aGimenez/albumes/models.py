from django.db import models
from artistas.models import Artista

# Create your models here.

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    anio_lanzamiento = models.PositiveIntegerField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo