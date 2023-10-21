from django.urls import path
from .views import EmpleadoApiView

urlpatterns = [
    path('crear/empleados', EmpleadoApiView.as_view()),
    path('listar/empleados', EmpleadoApiView.as_view()),
    path('actualizar/empleados/<int:pkid>/', EmpleadoApiView.as_view(),name='actualizar_vehiculo'),
    path('eliminar/empleados/<int:pkid>/delete/', EmpleadoApiView.as_view(),name='eliminar_vehiculo'),
]