from django.db import models

from Models.Categoria.models import Categoria
from Models.Marca.models import Marca


class Producto(models.Model):
    producto = models.CharField(max_length=80)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto
