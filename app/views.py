from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def productos(request):
    suscripciones = Suscripcion.objects.all()
    return render(request, 'app/productos.html', {"suscripcion":suscripciones})

def compra(request):
    return render(request, 'app/compra.html')

def contacto(request):
    return render(request,'app/contacto.html')

def servicios(request):
    return render(request, 'app/servicios.html')