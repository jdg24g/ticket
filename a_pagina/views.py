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


    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            formset = CustomItemPedidoFormSet(request.POST, instance=ticket)
            if formset.is_valid():
                formset.save()
                return redirect('detalle_ticket', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
        formset = CustomItemPedidoFormSet(instance=ticket)
    
    return render(request, 'a_pagina/editar_ticket.html', {
        'form': form,
        'formset': formset,
    })