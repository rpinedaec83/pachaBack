from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from artistas.models import Artista
from albumes.models import Album
from canciones.models import Cancion


class CancionCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artista = Artista.objects.create(nombre='Artista 1', genero='Rock')
        self.album = Album.objects.create(titulo='Álbum 1', anio_lanzamiento=2023, artista=self.artista)
        self.cancion = Cancion.objects.create(titulo='Canción 1', artista=self.artista, album=self.album)

    def test_list_canciones(self):
        url = reverse('canciones-list-create')
        response = self.client.get(url, {'titulo': 'Canción 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(url, {'titulo': 'Canción 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_cancion(self):
        url = reverse('canciones-list-create')
        data = {'titulo': 'Canción 2', 'artista': self.artista.id, 'album': self.album.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cancion.objects.count(), 2)

    def test_retrieve_cancion(self):
        url = reverse('canciones-retrieve-update-destroy', args=[self.cancion.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.cancion.titulo)

    def test_update_cancion(self):
        url = reverse('canciones-retrieve-update-destroy', args=[self.cancion.id])
        data = {'titulo': 'Nuevo Título'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cancion.refresh_from_db()
        self.assertEqual(self.cancion.titulo, 'Nuevo Título')

    def test_delete_cancion(self):
        url = reverse('canciones-retrieve-update-destroy', args=[self.cancion.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cancion.objects.count(), 0)

