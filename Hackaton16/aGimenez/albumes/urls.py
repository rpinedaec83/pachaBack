from django.urls import path
from albumes.views import AlbumListCreateView, AlbumRetrieveUpdateDestroyView


urlpatterns = [
    path('albumes/', AlbumListCreateView.as_view(), name='albumes-list-create'),
    path('albumes/<int:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='albumes-retrieve-update-destroy'),
]
