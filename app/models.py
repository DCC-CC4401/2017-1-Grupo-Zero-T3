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


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete="cascade")
    formas_de_pago = models.OneToOneField(FormasDePago, on_delete="cascade")

    class Meta:
        ordering = ["user.username"]

    def __str__(self):
        return self.user.username + ", " + self.user.email

    def pagos(self):
        return str(self.formas_de_pago)


class VendedorAmbulante(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete="cascade")

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()


class VendedorFijo(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete="cascade")

    hora_apertura = models.IntegerField()
    hora_clausura = models.IntegerField()
    ubicacion = models.CharField(max_length=60)

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()

    class Meta:
        ordering = ["user.username"]


class Producto(models.Model):
    vendedor = models.OneToOneField(Vendedor)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    precio = models.IntegerField(max_length=60)
    stock = models.IntegerField()

