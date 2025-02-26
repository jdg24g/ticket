from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

def imprimir_ticket(request):
    return HttpResponse("Imprimir ticket")

def vista_previa_ticket(request):
    return HttpResponse("Vista previa ticket")


