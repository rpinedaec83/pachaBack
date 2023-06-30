from django.urls import include, path

urlpatterns = [
    path('api/', include('artistas.urls')),
    path('api/', include('albumes.urls')),
    path('api/', include('canciones.urls')),
    path('api/', include('playlists.urls')),
    path('api/', include('usuarios.urls'))
]