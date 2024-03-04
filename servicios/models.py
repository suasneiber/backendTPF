from django.db import models
from insumos.models import Insumos

# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length= 20)
    insumo =models.ForeignKey(Insumos, on_delete = models.CASCADE)
    cantUso = models.IntegerField()
    Precio = models.FloatField()

    def __str__(self):
            return self.nombre