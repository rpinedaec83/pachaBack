from django.db import models
from artistas.models import Artista
from albumes.models import Album


class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)