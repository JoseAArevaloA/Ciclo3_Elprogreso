from django.db import models
from datetime import date


class Producto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    categoria= models.CharField(max_length=50, blank=False, null=False)
    descripción = models.TextField(max_length=500, blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    peso = models.CharField(max_length=50, blank=False, null=False, default= '500 g')
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre


opciones_consultas=[
    [0,'Consulta'],
    [1,'Reclamo'],
    [2,'Sugerencia'],
    [3,'Felicitaciones'],
]

class Mensaje(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=False,blank=False)
    tipo_consulta= models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre





