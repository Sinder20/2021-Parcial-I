from django import forms

from Models.Categoria.models import Categoria


class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
