from django import forms

from .models import Categoria

class CategoriaForm(forms.ModelForm):
    # Agrega los campos adicionales que deseas incluir en el formulario
    campo_adicional = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Categoria
        fields = ["nombre", "campo_adicional"]

