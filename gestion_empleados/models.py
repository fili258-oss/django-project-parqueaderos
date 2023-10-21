from django.db import models

# Create your models here.
class empleado(models.Model):
    identificacion = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    genero = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)