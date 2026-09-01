from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Actividad
from .serializers import ActividadSerializer


@api_view(['GET', 'POST'])
def actividades(request):

    if request.method == 'GET':

        actividades = Actividad.objects.all()

        serializer = ActividadSerializer(
            actividades,
            many=True
        )

        return Response(serializer.data)


    if request.method == 'POST':

        serializer = ActividadSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST', 'DELETE'])
def actividad_detalle(request, id):

    try:

        actividad = Actividad.objects.get(id=id)

    except Actividad.DoesNotExist:

        return Response(
            {'error': 'Actividad no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )


    # MODIFICAR ESTADO
    if request.method == 'POST':

        nuevo_estado = request.data.get('estado')

        estados_validos = [
            'Pendiente',
            'En proceso',
            'Completada'
        ]

        if nuevo_estado not in estados_validos:

            return Response(
                {'error': 'Estado no válido'},
                status=status.HTTP_400_BAD_REQUEST
            )

        actividad.estado = nuevo_estado
        actividad.save()

        serializer = ActividadSerializer(actividad)

        return Response(serializer.data)


    # ELIMINAR
    if request.method == 'DELETE':

        actividad.delete()

        return Response(
            {'mensaje': 'Actividad eliminada correctamente'}
        )