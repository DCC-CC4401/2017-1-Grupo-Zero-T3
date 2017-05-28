from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='media', default="img/avatarEstudiante3.png", blank=True)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return "Admin: " + self.user.username + ", " + self.user.email


class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='media', default="img/avatarPenguin.png", blank=True)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return "Alumno: " + self.user.username + ", " + self.user.email


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='media', default="img/avatarVendedor3.png", blank=True)

    credito = models.BooleanField(default=False)
    debito = models.BooleanField(default=False)
    efectivo = models.BooleanField(default=False)
    JUNAEB = models.BooleanField(default=False)

    activo = models.BooleanField(default=False)

    tipos = (
        (1, "fijo"),
        (2, "ambulante"),
    )
    tipo = models.IntegerField(choices=tipos, default=2)

    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username + ", " + self.user.email

    def pagos(self):
        cred = "credito, " if self.credito else ""
        deb = "debito, " if self.debito else ""
        efec = "efectivo, " if self.efectivo else ""
        jun = "JUNAEB, " if self.JUNAEB else ""
        return (cred + deb + efec + jun)[:-2]


class VendedorAmbulante(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()


class VendedorFijo(models.Model):
    vendedor = models.OneToOneField(Vendedor, on_delete=models.CASCADE)

    hora_apertura = models.IntegerField()
    hora_clausura = models.IntegerField()
    ubicacion = models.CharField(max_length=60)

    def __str__(self):
        return "Vendedor Ambulante: " + str(self.vendedor)

    def pagos(self):
        return self.vendedor.pagos()


class Producto(models.Model):
    vendedor = models.OneToOneField(Vendedor)

    foto = models.ImageField(upload_to='media', default="img/bread", blank=True)

    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()

    categorias = (
        (1, "normal"),
        (2, "vegetariano"),
        (3, "vegano"),
    )
    categoria = models.IntegerField(choices=categorias, default=1)

    class Meta:
        ordering = ["vendedor", "nombre"]

    def __str__(self):
        return "Producto: " + self.nombre + " $" + str(self.precio) + " q" + str(self.stock)


class Favorito(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["alumno", "vendedor"]

    def __str__(self):
        return self.alumno.user.username + " " + self.vendedor.user.username
