from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imprimir-ticket/<int:ticket_id>/', views.imprimir_ticket, name='imprimir_ticket'),
    path('vista-previa/<int:ticket_id>/', views.vista_previa_ticket, name='vista_previa_ticket'),
]
