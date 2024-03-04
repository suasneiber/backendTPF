from django.urls import path
from clientes.api.views import clienteList, clienteDetail

urlpatterns = [
    path('list/',clienteList.as_view(), name='clientelist'),
    path('<int:pk>',clienteDetail.as_view(), name='clientedetail')
]
