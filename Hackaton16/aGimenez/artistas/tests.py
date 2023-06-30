from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from artistas.models import Artista


class ArtistaCRUDTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.artista = Artista.objects.create(nombre='Artista 1', genero='Rock')

    def test_list_artistas(self):
        url = reverse('artistas-list-create')
        response = self.client.get(url, {'nombre': 'Artista 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_artista(self):
        url = reverse('artistas-list-create')
        data = {'nombre': 'Artista 2', 'genero': 'Pop'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artista.objects.count(), 2)

    def test_retrieve_artista(self):
        url = reverse('artistas-retrieve-update-destroy', args=[self.artista.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.artista.nombre)

    def test_update_artista(self):
        url = reverse('artistas-retrieve-update-destroy', args=[self.artista.id])
        data = {'nombre': 'Nuevo Nombre'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.artista.refresh_from_db()
        self.assertEqual(self.artista.nombre, 'Nuevo Nombre')

    def test_delete_artista(self):
        url = reverse('artistas-retrieve-update-destroy', args=[self.artista.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artista.objects.count(), 0)
