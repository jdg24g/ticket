from django.db import models
from django.utils import timezone

PRODUCTOS = [
    ("1", "Hamburguesa"),
    ("2", "Papas"),
    ("3", "Refresco"),
    ("4", "Helado"),
]

class Ticket(models.Model):
    cliente = models.CharField(max_length=100, null=True, blank=True)
    numero_mesa = models.IntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    es_delivery = models.BooleanField(default=False)
        


class ItemPedido(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    producto = models.CharField(max_length=100, choices=PRODUCTOS)
    monto = models.PositiveIntegerField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True)
    observaciones = models.TextField(null=True, blank=True)
    
