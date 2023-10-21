from .models import empleado
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = ['identificacion','nombre','edad','genero','telefono']