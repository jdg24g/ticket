# forms.py
from django import forms
from .models import Ticket, Cliente, ItemPedido

class TicketForm(forms.Form):
    tipo_cliente = forms.ChoiceField(
        choices=[('mesa', 'Mesa'), ('cliente', 'Cliente')],
        widget=forms.RadioSelect
    )
    numero_mesa = forms.IntegerField(required=False)
    nombre_cliente = forms.CharField(max_length=100, required=False)
    es_delivery = forms.BooleanField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        tipo_cliente = cleaned_data.get('tipo_cliente')
        
        if tipo_cliente == 'mesa' and not cleaned_data.get('numero_mesa'):
            self.add_error('numero_mesa', 'Debe especificar un número de mesa')
        
        if tipo_cliente == 'cliente' and not cleaned_data.get('nombre_cliente'):
            self.add_error('nombre_cliente', 'Debe especificar un nombre de cliente')
        
        return cleaned_data


# views.py (adicionales)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TicketForm
from .models import Cliente, Ticket, ItemPedido

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        
        if form.is_valid():
            # Procesar cliente/mesa
            tipo_cliente = form.cleaned_data['tipo_cliente']
            es_mesa = (tipo_cliente == 'mesa')
            
            if es_mesa:
                numero_mesa = form.cleaned_data['numero_mesa']
                # Buscar o crear mesa
                cliente, _ = Cliente.objects.get_or_create(
                    es_mesa=True,
                    numero_mesa=numero_mesa,
                    defaults={'nombre': f'Mesa {numero_mesa}'}
                )
            else:
                nombre_cliente = form.cleaned_data['nombre_cliente']
                cliente, _ = Cliente.objects.get_or_create(
                    es_mesa=False,
                    nombre=nombre_cliente,
                    defaults={'numero_mesa': None}
                )
            
            # Crear ticket
            ticket = Ticket.objects.create(
                cliente=cliente,
                es_delivery=form.cleaned_data['es_delivery']
            )
            
            # Procesar productos
            productos = request.POST.getlist('producto[]')
            cantidades = request.POST.getlist('cantidad[]')
            observaciones = request.POST.getlist('observaciones[]')
            
            for i in range(len(productos)):
                if productos[i].strip():  # Solo si hay un producto
                    ItemPedido.objects.create(
                        ticket=ticket,
                        producto=productos[i],
                        cantidad=int(cantidades[i]),
                        observaciones=observaciones[i] if i < len(observaciones) else None
                    )
            
            # Redireccionar a vista previa
            return redirect('vista_previa_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm()
    
    return render(request, 'crear_ticket.html', {'form': form})