from django.urls import path
from artistas.views import ArtistaListCreateView, ArtistaRetrieveUpdateDestroyView

urlpatterns = [
    path('artistas/', ArtistaListCreateView.as_view(), name='artistas-list-create'),
    path('artistas/<int:pk>/', ArtistaRetrieveUpdateDestroyView.as_view(), name='artistas-retrieve-update-destroy'),
]
