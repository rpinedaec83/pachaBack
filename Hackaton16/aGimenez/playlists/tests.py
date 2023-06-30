from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Playlist
from usuarios.models import Usuario
from canciones.models import Cancion
from artistas.models import Artista
from albumes.models import Album

class PlaylistAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = Usuario.objects.create(username='user1', email='user1@example.com', password='user1password')
        self.artista = Artista.objects.create(nombre='Artista 1', genero='Rock')
        self.album = Album.objects.create(titulo='Álbum 1', anio_lanzamiento=2023, artista=self.artista)
        self.cancion = Cancion.objects.create(titulo='Canción 1', artista=self.artista, album=self.album)
        self.playlist1 = Playlist.objects.create(titulo='Playlist 1', usuario=self.usuario)
        self.playlist1.canciones.set([self.cancion])
        self.playlist2 = Playlist.objects.create(titulo='Playlist 2', usuario=self.usuario)
        self.playlist2.canciones.set([self.cancion])


    def test_list_playlists(self):
        url = reverse('playlist-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_playlist(self):
        url = reverse('playlist-retrieve-update-destroy', args=[self.playlist1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], 'Playlist 1')

    def test_create_playlist(self):
        url = reverse('playlist-list-create')
        data = {'titulo': 'Playlist 3', 'usuario': self.usuario.id, 'canciones': [self.cancion.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 3)
        self.assertEqual(Playlist.objects.latest('id').titulo, 'Playlist 3')

    def test_update_playlist(self):
        url = reverse('playlist-retrieve-update-destroy', args=[self.playlist1.id])
        data = {'titulo': 'Updated Playlist 1'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Playlist.objects.get(id=self.playlist1.id).titulo, 'Updated Playlist 1')

    def test_delete_playlist(self):
        url = reverse('playlist-retrieve-update-destroy', args=[self.playlist1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Playlist.objects.count(), 1)
        self.assertFalse(Playlist.objects.filter(id=self.playlist1.id).exists())
