from django.http import HttpResponse
from AppGoldenCafe.models import Cliente


def funcion(req):
    return HttpResponse("Vamos bien")

def agregar_cliente(req, nombre_cliente, email_cliente):
    cliente = Cliente(nombre = nombre_cliente, email = email_cliente)
    cliente.save()

    return HttpResponse("Cliente agregado!")