from rest_framework import generics
from artistas.models import Artista
from artistas.serializers import ArtistaSerializer


class ArtistaListCreateView(generics.ListCreateAPIView):
    serializer_class = ArtistaSerializer
    def get_queryset(self):
        queryset = Artista.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset

class ArtistaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
