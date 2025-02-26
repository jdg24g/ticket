from django import forms
from django.forms import inlineformset_factory
from .models import Ticket, ItemPedido, Cliente, Producto

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['tipo', 'cliente', 'mesa', 'observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1}),
        }

# Creamos un formset para manejar múltiples ItemPedido en un solo formulario
ItemPedidoFormSet = inlineformset_factory(
    Ticket, 
    ItemPedido,
    form=ItemPedidoForm,
    extra=1,  # Número de formularios vacíos
    can_delete=True  # Permite eliminar items
)

# Si quieres implementar la lógica de mostrar extra=1 solo cuando no hay items:
class CustomItemPedidoFormSet(ItemPedidoFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si estamos editando un ticket existente con items
        if self.instance and self.instance.pk and self.instance.itempedido_set.exists():
            self.extra = 0
        else:
            self.extra = 1