from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_marca/', views.agregar_marca, name='agregar_marca'),
    path('agregar_moto/', views.agregar_moto, name='agregar_moto'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('buscar_moto/', views.buscar_moto, name='buscar_moto'),
]
