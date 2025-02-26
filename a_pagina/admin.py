from django.contrib import admin
from .models import Producto, Cliente, Ticket, ItemPedido

class ItemPedidoInline(admin.TabularInline):  # También puedes usar admin.StackedInline
    model = ItemPedido
    extra = 0  # Por defecto no mostrar campos extra
    
    def get_extra(self, request, obj=None, **kwargs):
        # Si obj es None, estamos creando un nuevo Ticket
        # Si obj existe pero no tiene items, también mostramos un campo extra
        if obj is None or not obj.itempedido_set.exists():
            return 1
        return 0  # En otros casos, no mostrar campos extra



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ['id', 'cliente', 'tipo', 'fecha_creacion']

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(ItemPedido)