from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Usuario


class UsuarioTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_usuario(self):
        url = reverse('usuario-list')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 1)
        self.assertEqual(Usuario.objects.get().username, 'testuser')

    def test_get_usuario_list(self):
        Usuario.objects.create(username='user1', email='user1@example.com', password='user1password')
        Usuario.objects.create(username='user2', email='user2@example.com', password='user2password')
        url = reverse('usuario-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_usuario(self):
        usuario = Usuario.objects.create(username='user', email='user@example.com', password='userpassword')
        url = reverse('usuario-detail', args=[usuario.id])
        data = {
            'username': 'updateduser',
            'email': 'updated@example.com',
            'password': 'updatedpassword'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Usuario.objects.get().username, 'updateduser')

    def test_delete_usuario(self):
        usuario = Usuario.objects.create(username='user', email='user@example.com', password='userpassword')
        url = reverse('usuario-detail', args=[usuario.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Usuario.objects.count(), 0)
