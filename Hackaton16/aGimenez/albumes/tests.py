from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from artistas.models import Artista
from albumes.models import Album


class AlbumCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artista = Artista.objects.create(nombre='Artista 1', genero='Rock')
        self.album = Album.objects.create(titulo='Álbum 1', anio_lanzamiento=2023, artista=self.artista)

    def test_list_albumes(self):
        url = reverse('albumes-list-create')
        response = self.client.get(url, {'titulo': 'Álbum 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_album(self):
        url = reverse('albumes-list-create')
        data = {'titulo': 'Álbum 2', 'anio_lanzamiento': 2022, 'artista': self.artista.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.count(), 2)

    def test_retrieve_album(self):
        url = reverse('albumes-retrieve-update-destroy', args=[self.album.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.album.titulo)

    def test_update_album(self):
        url = reverse('albumes-retrieve-update-destroy', args=[self.album.id])
        data = {'titulo': 'Nuevo Título'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.album.refresh_from_db()
        self.assertEqual(self.album.titulo, 'Nuevo Título')

    def test_delete_album(self):
        url = reverse('albumes-retrieve-update-destroy', args=[self.album.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 0)
