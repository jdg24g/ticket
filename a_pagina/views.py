from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'index.html')


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