from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=60, help_text="Ingrese su nombre")

    password = models.CharField(max_length=60, help_text="Ingrese su contraseña")

    mail = models.EmailField(max_length=60, help_text="Ingrese su mail")

    USER_TYPE = (
        ('AD', 'admin'),
        ('AL', 'alumno'),
        ('VA', 'vendedor ambulante'),
        ('VF', 'vendedor fijo'),
    )
    user_type = models.CharField(max_length=2, choices=USER_TYPE)

    class Meta:
        ordering = ["user_type", "nombre"]

    def __str__(self):
        return self.nombre + " " + self.mail + " " + self.user_type
