from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=15)
    cargaHs = models.CharField(max_length=2)
    costo = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre