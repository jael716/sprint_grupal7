from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
class Prioridad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
"""

class Tarea(models.Model):    
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('EP', 'En Progreso'),
        ('C', 'Completada'),
    ]
    
    LABEL_CHOICES = [
        ('T', 'Trabajo'),
        ('H', 'Hogar'),
        ('E', 'Estudio'),
    ]

    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')
    #prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=2 , choices=ESTADO_CHOICES , default='P')
    label = models.CharField(max_length=1,choices=LABEL_CHOICES)


    def __str__(self):
        return self.titulo
    
    
