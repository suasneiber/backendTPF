from rest_framework import serializers
from clientes.models import Clientes

class ClienteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = "__all__"
