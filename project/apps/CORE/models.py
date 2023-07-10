from django.db import models

class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    mail = models.EmailField()
    telefono = models.CharField(max_length=20)

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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    condicion = models.CharField(max_length=100)
    eslora = models.DecimalField(max_digits=5, decimal_places=2)
    manga = models.DecimalField(max_digits=5, decimal_places=2)
    puntal = models.DecimalField(max_digits=5, decimal_places=2)
    astillero = models.CharField(max_length=100)
    anio_fabricacion = models.IntegerField()
    motorizacion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    comentario = models.TextField()

    def __str__(self):
        return f"{self.usuario} - {self.astillero} {self.anio_fabricacion}"


# Create your models here.

