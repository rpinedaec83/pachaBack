from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Tipo
from .serializers import TipoSerializer,MarcaSerializer,AutoSerializer
# Create your views here.
class TipoViewSet(viewsets.ModelViewSet):
    queryset= Tipo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TipoSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset= Tipo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=MarcaSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset= Tipo.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=AutoSerializer