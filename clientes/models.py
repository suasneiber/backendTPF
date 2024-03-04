from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=15)


    def __str__(self):
        return self.nombre