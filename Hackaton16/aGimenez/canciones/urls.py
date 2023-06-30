from django.urls import path
from canciones.views import CancionListCreateView, CancionRetrieveUpdateDestroyView

urlpatterns = [
    path('canciones/', CancionListCreateView.as_view(), name='canciones-list-create'),
    path('canciones/<int:pk>/', CancionRetrieveUpdateDestroyView.as_view(), name='canciones-retrieve-update-destroy'),
]
