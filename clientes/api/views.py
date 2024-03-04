from rest_framework import generics
from clientes.api.serializers import ClienteSerialiser
from clientes.models import Clientes

class clienteList(generics.ListCreateAPIView):
    queryset=Clientes.objects.all()
    serializer_class= ClienteSerialiser

class clienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Clientes.objects.all() 
    serializer_class=ClienteSerialiser
