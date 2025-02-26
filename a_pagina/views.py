from django.shortcuts import render, redirect, get_object_or_404
from .models import ItemPedido, Ticket

def index(request):
    title = 'BIDMAX'
    tickets = Ticket.objects.all().order_by('-fecha_creacion')  # Ordenado por fecha, más reciente primero
    context = {
        'title': title,
        'items': tickets,  # Pasamos los tickets como items
    }
    return render(request, 'index.html', context)

def detalle_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    items = ItemPedido.objects.filter(ticket=ticket)
    total = sum(item.producto.precio * item.cantidad for item in items)
    context = {
        'ticket': ticket,
        'items': items,
        'total': total,
    }
    return render(request, 'detalle_ticket.html', context)