from django.urls import path
from .views import UsuarioViewSet

urlpatterns = [
    path('usuarios/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usuario-detail'),
]
