from django.contrib import admin

# Register your models here.
from django.contrib import admin

from gestion_vehiculos.models import vehiculo


# Register your models here.

@admin.register(vehiculo)
class vehiculo_admin(admin.ModelAdmin):
    list_display=['placa', 'marca', 'imagen']