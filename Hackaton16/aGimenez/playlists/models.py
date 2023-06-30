from django.db import models
from canciones.models import Cancion
from usuarios.models import Usuario


class Playlist(models.Model):
    titulo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    canciones = models.ManyToManyField(Cancion)