from django.db import models

# Create your models here.
class Insumos(models.Model):
    nombre = models.CharField(max_length=20)
    stock = models.IntegerField()
    precioCosto = models.FloatField()
    cantUso = models.IntegerField()

    def __str__(self):
        return self.nombre