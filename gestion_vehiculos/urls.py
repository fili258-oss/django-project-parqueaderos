from django.urls import path
from .views import VehiculoApiView

urlpatterns = [
    path('vehiculos', VehiculoApiView.as_view()),
    path('vehiculos/<int:pkid>/', VehiculoApiView.as_view(),name='actualizar_vehiculo'),
    path('vehiculos/<int:pkid>/delete/', VehiculoApiView.as_view(),name='eliminar_vehiculo'),
]