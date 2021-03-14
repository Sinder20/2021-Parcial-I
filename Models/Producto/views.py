from django.http import HttpRequest
from django.shortcuts import render

from Models.Producto.forms import FormularioProducto
from Models.Producto.models import Producto


class FormularioProductoView(HttpRequest):

    def index(request):
        producto = FormularioProducto()
        return  render(request, "ProductoIndex.html", {"form":producto})

    def procesar_formulario(request):
        producto = FormularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto()

        return render(request, "ProductoIndex.html", {"form":producto, "mensaje": 'OK'})

    def listar_producto(request):
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos":productos})

    def editProducto(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(instance=producto)
        return render(request, "ProductoEdit.html", {"form":form, 'prodcuto':producto})

    def actualizar_producto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos":productos})

    def deleteProducto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        productos = Producto.objects.all()
        return render(request, "ListaProducto.html", {"productos":productos, "mensaje": 'OK'})