from django import forms

from .models import Categoria, Producto, Usuario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["motor", "vela", "auxiliar", "jet_ski_o_moto_de_agua", "remo"]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["usuario", "categoria", "condicion", "eslora", "manga", "puntal", "astillero",
                 "anio_fabricacion", "motorizacion", "capacidad", "ubicacion", "estado", "comentario"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'nombre_completo', 'mail', 'telefono', 'direccion' ]
    