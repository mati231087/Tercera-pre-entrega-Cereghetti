from django import forms

from .models import Categoria, Producto, Usuario

class CategoriaForm(forms.ModelForm):
    # Agrega los campos adicionales que deseas incluir en el formulario
    campo_adicional = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Categoria
        fields = ["nombre", "campo_adicional"]

class UsuarioForm(forms.ModelForm):

    
    class Meta:
        model = Usuario
        fields = ["nombre_completo", "mail", "telefono"]

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["usuario", "categoria", "condicion", "eslora", "manga", "puntal", "astillero", "año_fabricacion", "motorizacion", "capacidad", "ubicacion", "estado", "comentario"]