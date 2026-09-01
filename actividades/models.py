from django.db import models


class Actividad(models.Model):

    TIPO_CHOICES = [
        ('Academica', 'Académica'),
        ('Administrativa', 'Administrativa'),
    ]

    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completada', 'Completada'),
    ]

    aprendiz = models.CharField(max_length=100)
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='Pendiente'
    )

    def __str__(self):
        return self.nombre