from django.shortcuts import render
from .forms import *
from .models import Moto

def inicio(request):
    return render(request, "main/inicio.html")

from django.contrib import messages

from django.contrib import messages
from django.shortcuts import render

def agregar_marca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marca agregada con éxito.")
            form = MarcaForm()  # Reinicia el formulario vacío
    else:
        form = MarcaForm()
    return render(request, "tienda/formulario.html", {
        "form": form,
        "titulo": "Agregar Marca"
    })

def agregar_moto(request):
    if request.method == "POST":
        form = MotoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Moto agregada con éxito.")
            form = MotoForm()
    else:
        form = MotoForm()
    return render(request, "tienda/formulario.html", {
        "form": form,
        "titulo": "Agregar Moto"
    })

def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente agregado con éxito.")
            form = ClienteForm()
    else:
        form = ClienteForm()
    return render(request, "tienda/formulario.html", {
        "form": form,
        "titulo": "Agregar Cliente"
    })

def buscar_moto(request):
    resultado = []
    form = BuscarMotoForm(request.GET or None)
    if form.is_valid():
        filtro = form.cleaned_data['filtro']
        query = form.cleaned_data['query']
        if filtro == 'marca':
            resultado = Moto.objects.filter(marca__nombre__icontains=query)
        elif filtro == 'modelo':
            resultado = Moto.objects.filter(modelo__icontains=query)
        elif filtro == 'cilindrada':
            resultado = Moto.objects.filter(cilindrada__icontains=query)
        elif filtro == 'año':
            resultado = Moto.objects.filter(año__icontains=query)
        elif filtro == 'estado':
            resultado = Moto.objects.filter(estado__icontains=query)
        elif filtro == 'kilometros':
            resultado = Moto.objects.filter(kilometros__icontains=query)
    return render(request, "tienda/buscar.html", {
        "form": form,
        "resultado": resultado
    })
