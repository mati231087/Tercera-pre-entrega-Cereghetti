
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(
        max_length=12,
        validators=[
            MinLengthValidator(8, 'La contraseña debe tener al menos 8 caracteres.'),
            MaxLengthValidator(12, 'La contraseña no puede tener más de 12 caracteres.'),
            RegexValidator(
                regex='.*[0-9].*',
                message='La contraseña debe contener al menos un número.'
            )
        ]
    )

    def __str__(self):
        return self.username

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='productos')
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre

