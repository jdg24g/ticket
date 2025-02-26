from django.contrib import admin
from .models import Producto, Cliente, Ticket, ItemPedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Ticket)
admin.site.register(ItemPedido)

