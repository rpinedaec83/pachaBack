from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField(max_length=100)
    # Otros campos para el modelo de usuario


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
