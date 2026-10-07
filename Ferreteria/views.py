from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all().order_by('id')
    return render(request, 'Ferreteria/lista_productos.html', {'productos': productos})