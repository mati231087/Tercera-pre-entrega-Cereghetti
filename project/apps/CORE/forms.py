from django import forms

from .models import Categoria, Producto, Usuario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]

