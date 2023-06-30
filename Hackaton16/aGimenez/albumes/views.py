from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer


class AlbumListCreateView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    def get_queryset(self):
        queryset = Album.objects.all()
        titulo = self.request.query_params.get('titulo')
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        return queryset


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
