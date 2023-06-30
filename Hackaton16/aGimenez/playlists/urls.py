from django.urls import path
from playlists.views import PlaylistListCreateView, PlaylistRetrieveUpdateDestroyView

urlpatterns = [
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list-create'),
    path('playlists/<int:pk>/', PlaylistRetrieveUpdateDestroyView.as_view(), name='playlist-retrieve-update-destroy'),
]
