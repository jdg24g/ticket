from django import forms
from .models import Ticket, ItemPedido

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