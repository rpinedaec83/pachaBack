from rest_framework import generics
from .models import Cancion
from .serializers import CancionSerializer

class CancionListCreateView(generics.ListCreateAPIView):
    serializer_class = CancionSerializer
    def get_queryset(self):
        queryset = Cancion.objects.all()
        titulo = self.request.query_params.get('titulo')
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        return queryset

class CancionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cancion.objects.all()
    serializer_class = CancionSerializer

