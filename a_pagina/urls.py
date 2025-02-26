from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:pk>/', views.detalle_ticket, name='detalle_ticket'),
]
