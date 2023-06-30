from rest_framework import serializers
from canciones.models import Cancion


class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = '__all__'