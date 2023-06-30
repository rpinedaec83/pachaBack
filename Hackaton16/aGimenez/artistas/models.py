from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre