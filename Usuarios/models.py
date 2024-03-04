from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre
