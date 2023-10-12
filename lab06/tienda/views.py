from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

categorias = Categoria.objects.distinct()

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    context = {'product_list' : product_list, 'categorias' : categorias}
    return render(request, 'index.html', context)
    
def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto' : producto, 'categorias' : categorias})

def listado(request,producto_cat):
    productos = Producto.objects.filter(categoria__nombre=producto_cat)
    return render(request, 'lista.html', {'productos' :productos, 'categorias' : categorias})