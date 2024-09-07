from django.db import models


class Cliente(models.Model):   
    nombre = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email}"

class Pedido(models.Model):   
    tipo_cafe = models.CharField(max_length=30)
    unidades = models.IntegerField()

    def __str__(self):
        return f"Pedido: {self.tipo_cafe} - Unidades: {self.unidades}"

class Sucursal(models.Model):   
    barrio = models.CharField(max_length=30)
    id_sucursal = models.IntegerField()

    def __str__(self):
        return f"Barrio/Sucursal: {self.barrio} - ID Sucursal: {self.id_sucursal}"

