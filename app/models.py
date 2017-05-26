from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")

    class Meta:
        ordering = ["user.username"]

    def __str__(self):
        return "Admin: " + self.user.username + ", " + self.user.email


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")

    class Meta:
        ordering = ["user.username"]

    def __str__(self):
        return "Alumno: " + self.user.username + ", " + self.user.email


class FormasDePago(models.Model):
    credito = models.BooleanField(default=False)
    dedito = models.BooleanField(default=False)
    efectivo = models.BooleanField(default=False)
    JUNAEB = models.BooleanField(default=False)

    def __str__(self):
        cred = "credito, " if self.credito else ""
        deb = "debito, " if self.debito else ""
        efec = "efectivo, " if self.efectivo else ""
        jun = "JUNAEB, " if self.JUNAEB else ""
        return (cred + deb + efec + jun)[:-2]


class VendedorAmbulante(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")
    formas_de_pago = models.OneToOneField(FormasDePago, on_delete="cascade")

    class Meta:
        ordering = ["user.username"]

    def __str__(self):
        return "Vendedor Ambulante: " + self.user.username + ", " + self.user.email

    def pagos(self):
        return str(self.formas_de_pago)


class VendedorFijo(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")
    formas_de_pago = models.OneToOneField(FormasDePago, on_delete="cascade")

    hora_apertura = models.IntegerField()
    hora_clausura = models.IntegerField()
    ubicacion = models.CharField(max_length=60)

    class Meta:
        ordering = ["user.username"]

    def __str__(self):
        return "Vendedor Fijo: " + self.user.username + ", " + self.user.email

    def pagos(self):
        return str(self.formas_de_pago)


