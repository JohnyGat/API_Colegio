from django.urls import path
from . import views


urlpatterns = [

    path(
        'actividades/',
        views.actividades,
        name='actividades'
    ),

    path(
        'actividades/<int:id>/',
        views.actividad_detalle,
        name='actividad_detalle'
    ),

]