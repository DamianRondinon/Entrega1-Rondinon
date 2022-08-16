from django.shortcuts import render, redirect
from productos.models import Producto
from productos.forms import FormularioBusqueda
from productos.forms import FormularioAgregar
# Create your views here.


def index(request):


    listado_productos = Producto.objects.all()

    if request.GET.get("nombre_producto"):

        formulario = FormularioBusqueda(request.GET)
        if formulario.is_valid():
           data = formulario.cleaned_data
           listado_productos = Producto.objects.filter(nombre__icontains = data["nombre_producto"])

           

        return render(request, "productos/index.html", {"productos": listado_productos})
    
    else:
        formulario = FormularioBusqueda()
        return render(request, "productos/index.html", {"productos": listado_productos, "formulario": formulario})



def crearProducto(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    marca = request.POST["marca"]

    producto=Producto.objects.create(nombre=nombre, precio=precio, marca=marca)
    return redirect("/")

