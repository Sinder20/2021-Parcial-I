"""RegistroProductos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Categoria.views import FormularioCategoriaView
from Models.Marca.views import FormularioMarcaView
from Models.Producto.views import FormularioProductoView
from Views.HomeView import HomeView

urlpatterns = [
 #   path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('formulario/', HomeView.formulario, name='formulario'),
    path('registrarMarca/', FormularioMarcaView.index, name='registrarMarca'),
    path('guardarMarca/', FormularioMarcaView.procesar_formulario, name='guardarMarca'),
    path('registrarCategoria/', FormularioCategoriaView.index, name='registrarCategoria'),
    path('guardarCategoria/', FormularioCategoriaView.procesar_formulario, name='guardarCategoria'),
    path('registrarProducto/', FormularioProductoView.index, name='registrarProducto'),
    path('guardarProducto', FormularioProductoView.procesar_formulario, name='guardarProducto'),
    path('listarMarcas/', FormularioMarcaView.listar_marca, name='listarMarcas'),
    path('listarCategorias/', FormularioCategoriaView.listar_categoria, name='listarCategoria'),
    path('listarProductos/', FormularioProductoView.listar_producto, name='listarProductos'),
    path('editarMarca/<int:id_marca>', FormularioMarcaView.editMarca, name='editarMarca'),
    path('actualizarMarca/<int:id_marca>', FormularioMarcaView.actualizar_marca, name='actualizarMarca'),
    path('editarCategoria/<int:id_categoria>', FormularioCategoriaView.editCategoria, name='editarCategoria'),
    path('actualizarCategoria/<int:id_categoria>', FormularioCategoriaView.actualizar_categoria, name='actualizarCategoria'),
    path('editarProducto/<int:id_producto>', FormularioProductoView.editProducto, name='editarProducto'),
    path('actualizarProducto/<int:id_producto>', FormularioProductoView.actualizar_producto, name='actualizarProducto'),
    path('eliminarMarca/<int:id_marca>', FormularioMarcaView.deleteMarca, name='eliminarMarca'),
    path('eliminarCategoria/<int:id_categoria>', FormularioCategoriaView.deleteCategoria, name='eliminarCategoria'),
    path('eliminarProducto/<int:id_producto>', FormularioProductoView.deleteProducto, name='eliminarProducto'),
]
