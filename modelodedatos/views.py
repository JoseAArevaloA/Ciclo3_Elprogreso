from django.shortcuts import render
from .forms import *
from .models import *


def productos(request):
    productos = Producto.objects.all()
    contexto= {'productos': productos}
    return render(request, 'productos.html',contexto)

def contactenos(request):

    if request.method == 'POST':
        mensajes= MensajeForm(request.POST)
        if mensajes.is_valid():
            mensajes.save()
        return render(request, 'contactenos.html',{'mensajes':mensajes})
    else:
        mensajes= MensajeForm()
        return render(request, 'contactenos.html',{'mensajes':mensajes})





