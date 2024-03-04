from django.db import models
from clientes.models import Clientes
from servicios.models import Servicios
# Create your models here.
class regServicio (models.Model):
    nomCliente = models.ForeignKey(Clientes, on_delete= models.CASCADE, related_name='clientes')
    nomServicio = models.ForeignKey(Servicios, on_delete = models.CASCADE)
    dia = models.DateField(null=True)
    hora = models.TimeField(null=True)

    def __str__(self):
        return self.nomCliente.nombre
