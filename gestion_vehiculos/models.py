from django.db import models

# Create your models here.
class vehiculo(models.Model):
    placa = models.CharField(max_length=6)
    modelo = models.IntegerField(default=2000)
    color = models.CharField(max_length=10)
    marca = models.CharField(max_length=20)
    imagen = models.URLField("De imdb mismo")
