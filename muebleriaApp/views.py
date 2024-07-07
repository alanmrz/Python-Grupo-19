from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto , Carrito
def template(request):
    return render(request, 'template.html')

def nosotros(request):
    return render(request, 'nosotros.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def agregar_a_carrito(request, producto_id, cantidad):
    producto = get_object_or_404(Producto, id=producto_id)
    item_carrito, created = Carrito.objects.get_or_create(producto=producto)
    
    if created:
        item_carrito.cantidad = int(cantidad)
    else:
        item_carrito.cantidad += int(cantidad)
    
    item_carrito.save()
    return redirect('ver_carrito')

def editar_carrito(request, carrito_id):
    item_carrito = get_object_or_404(Carrito, id=carrito_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad', 1))
        item_carrito.cantidad = cantidad
        item_carrito.save()
        return redirect('ver_carrito')
    return render(request, 'editar_carrito.html', {'item': item_carrito})

def eliminar_del_carrito(request, carrito_id):
    item_carrito = get_object_or_404(Carrito, id=carrito_id)
    item_carrito.delete()
    return redirect('ver_carrito')

def ver_carrito(request):
    items = Carrito.objects.all()
    return render(request, 'carrito.html', {'carrito': items})
