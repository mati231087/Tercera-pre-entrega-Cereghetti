from django import forms

from .models import Categoria, Producto, Usuario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["usuario", "categoria", "condicion", "eslora", "manga", "puntal", "astillero",
                 "anio_fabricacion", "motorizacion", "capacidad", "ubicacion", "estado", "comentario"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'mail', 'telefono']
