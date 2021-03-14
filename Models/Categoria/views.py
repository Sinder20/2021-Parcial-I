from django.http import HttpRequest
from django.shortcuts import render

from Models.Categoria.forms import FormularioCategoria
from Models.Categoria.models import Categoria


class FormularioCategoriaView(HttpRequest):

    def index(request):
        categoria = FormularioCategoria()
        return  render(request, "CategoriaIndex.html", {"form":categoria})

    def procesar_formulario(request):
        categoria = FormularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategoria()

        return render(request, "CategoriaIndex.html", {"form":categoria, "mensaje": 'OK'})

    def listar_categoria(request):
        categorias = Categoria.objects.all()
        return render(request, "ListaCategoria.html", {"categorias":categorias})

    def editCategoria(request, id_categoria):
        categoria = Categoria.objects.filter(id=id_categoria).first()
        form = FormularioCategoria(instance=categoria)
        return render(request, "CategoriaEdit.html", {"form":form, 'categoria':categoria})

    def actualizar_categoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        form = FormularioCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        categorias = Categoria.objects.all()
        return render(request, "ListaCategoria.html", {"categorias":categorias})

    def deleteCategoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        categoria.delete()
        categorias = Categoria.objects.all()
        return render(request, "ListaCategoria.html", {"categorias":categorias, "mensaje": 'OK'})
