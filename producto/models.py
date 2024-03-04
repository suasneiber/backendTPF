from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length= 20)
    precioCosto = models.FloatField()
    Porcentaje = models.FloatField()

    def __str__(self):
        return self.nombre