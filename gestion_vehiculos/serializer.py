from .models import vehiculo
from rest_framework import serializers

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = ['placa','modelo','marca','color','imagen']