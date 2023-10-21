from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmpleadoSerializer
from .models import empleado
import json

from django.shortcuts import render
# Create your views here.

class EmpleadoApiView(APIView):
    def get(self, request, *args, **kwargs):
        lista_empleados = empleado.objects.all()
        serializador = EmpleadoSerializer(lista_empleados, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'identificacion':request.data.get('identificacion'),
            'nombre':request.data.get('nombre'),
            'edad':request.data.get('edad'),
            'genero':request.data.get('genero'),
            'telefono':request.data.get('telefono')
        }
        serializador = EmpleadoSerializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        mi_empleado = empleado.objects.filter(id=pkid).update(
            identificacion = request.data('identificacion'),
            nombre = request.data('nombre'),
            edad = request.data('edad'),
            genero = request.data('genero'),
            telefono = request.data('telefono')
        )
        return Response(mi_empleado, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid, *args, **kwargs):
        mi_empleado = empleado.objects.filter(id=pkid)
        if not mi_empleado:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            mi_empleado.delete()
            return Response(mi_empleado, status=status.HTTP_200_OK)