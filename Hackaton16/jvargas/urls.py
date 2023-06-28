from django.urls import path
from myapp.views import (
    ArtistListCreateView, ArtistRetrieveUpdateDestroyView,
    AlbumListCreateView, AlbumRetrieveUpdateDestroyView,
    SongListCreateView, SongRetrieveUpdateDestroyView,
    UserListCreateView, UserRetrieveUpdateDestroyView,
    PlaylistListCreateView, PlaylistRetrieveUpdateDestroyView
)

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail'),
    path('albums/', AlbumListCreateView.as_view(), name='album-list'),
    path('albums/<int:pk>/', AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail'),
    path('songs/', SongListCreateView.as_view(), name='song-list'),
    path('songs/<int:pk>/', SongRetrieveUpdateDestroyView.as_view(), name='song-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('playlists/', PlaylistListCreateView.as_view(), name='playlist-list'),
    path('playlists/<int:pk>/', PlaylistRetrieveUpdateDestroyView.as_view(), name='playlist-detail'),
]
