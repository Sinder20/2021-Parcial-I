from django import forms

from Models.Marca.models import Marca


class FormularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        