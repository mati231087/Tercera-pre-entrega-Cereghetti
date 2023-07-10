from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100, default="sin nombre")
    mail = models.EmailField(default="example@example.com")
    telefono = models.CharField(max_length=20, default="sin telefono")

    def __str__(self):
        return self.nombre_completo


class Categoria(models.Model):
    OPCIONES_CATEGORIA = [
        ('motor', 'Embarcación a motor'),
        ('vela', 'Embarcación a vela'),
        ('moto_agua', 'Moto de agua'),
        ('jet_ski', 'Jet Ski'),
        ('remo', 'Embarcación a remo')
    ]

    nombre = models.CharField(max_length=50, choices=OPCIONES_CATEGORIA)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    usuario = models.CharField(max_length=100, default="")
    categoria = models.CharField(max_length=100, default="sin categoria")
    condicion = models.CharField(max_length=100, default="sin condicion")
    eslora = models.FloatField(default=0)
    manga = models.FloatField(default=0)
    puntal = models.FloatField(default=0)
    astillero = models.CharField(max_length=100, default="sin astillero")
    anio_fabricacion = models.IntegerField(
    default=0,
    validators=[
        MinValueValidator(1900, 'El año de fabricación debe ser igual o mayor a 1900.'),
        MaxValueValidator(timezone.now().year, 'El año de fabricación no puede ser mayor al año actual.')
    ]
)

    motorizacion = models.CharField(max_length=100, default="sin motorizacion")
    capacidad = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    ubicacion = models.CharField(max_length=100, default="sin ubicacion")
    estado = models.CharField(max_length=100, default="sin estado")
    comentario = models.TextField(max_length=1500, default="")

    def __str__(self):
        return f"{self.usuario} - {self.astillero} {self.anio_fabricacion}"


# Create your models here.

