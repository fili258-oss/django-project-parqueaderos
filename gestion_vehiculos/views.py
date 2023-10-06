from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import VehiculoSerializer
from .models import vehiculo
import json

from django.shortcuts import render

# Create your views here.

class VehiculoApiView(APIView):

    def get(self, request, *args, **kwargs):
        lista_vehiculos = vehiculo.objects.all()
        serializador = VehiculoSerializer(lista_vehiculos, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'placa':request.data.get('placa'),
            'marca':request.data.get('marca'),
            'modelo':request.data.get('modelo'),
            'color':request.data.get('color'),
            'imagen':request.data.get('imagen')
        }
        serializador = VehiculoSerializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid):
        mi_carro = vehiculo.objects.filter(id=pkid).update(
            placa = request.data('placa'),
            marca = request.data('marca'),
            modelo = request.data('modelo'),
            color = request.data('color'),
            imagen = request.data('imagen')
        )
        return Response(mi_carro, status=status.HTTP_200_OK)
    
    def delete(self, request, pkid, *args, **kwargs):
        mi_carro = vehiculo.objects.filter(id=pkid)
        if not mi_carro:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            mi_carro.delete()
            return Response(mi_carro, status=status.HTTP_200_OK)

