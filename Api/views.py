from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductoForm

def home(request):
    productos = Productos.objects.all()
    return render(request, 'home.html')

def listaProductos(request):
    productos = Productos.objects.all()
    return render(request, 'listaProductos.html', {'productos': productos})

def agregarProducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')
    else:
        form = ProductoForm()
    return render(request, 'agregarProducto.html', {'form': form})

def editarProducto(request, codigo):
    producto = Productos.objects.get(Codigo=codigo)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listaProductos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editarProducto.html', {'form': form})

def eliminarProducto(request, codigo):
    producto = Productos.objects.get(Codigo=codigo)
    if request.method == "POST":
        producto.delete()
        return redirect('listaProductos')
    return render(request, 'eliminarProducto.html', {'producto': producto})

            
        


