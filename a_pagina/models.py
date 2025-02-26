from django.db import models
from django.utils import timezone

tipo = [
    ("Delivery", "Delivery"),
    ("Mesa", "Mesa"),
    ("Recoger", "Recoger"),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveBigIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)


    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=100, null=True, blank=True)
    coordenadas = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ticket(models.Model):
    tipo = models.CharField(max_length=100, choices=tipo,default=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    mesa = models.PositiveIntegerField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    productos = models.ManyToManyField(Producto, through='ItemPedido')
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.cliente.nombre}"

    def get_total(self):
        return sum(item.cantidad * item.producto.precio for item in self.itempedido_set.all())


class ItemPedido(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    
    
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    
