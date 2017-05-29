from django import forms

from .models import VendedorAmbulante
from .models import VendedorFijo
from .models import Alumno

class LoginForm(forms.Form):
    username = forms.CharField(label="username", widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value=False))


class VendedorAmbulanteForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value=True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': 'validate'}))
    file = forms.FileField()
    CHOICES = (('Credito', 'Credito'),
               ('Debito', 'Debito'),
               ('Efectivo', 'Efectivo'),
               ('JUNAEB', 'JUNAEB'))
    credito = forms.BooleanField(
        label='credito',
        required=False,
        initial=False
    )
    efectivo = forms.BooleanField(
        label='efectivo',
        required=False,
        initial=True
    )
    debito = forms.BooleanField(
        label='debito',
        required=False,
        initial=False
    )
    junaeb = forms.BooleanField(
        label='JUNAEB',
        required=False,
        initial=False
    )


class VendedorFijoForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value=True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': 'validate'}))
    file = forms.FileField()
    CHOICES = (('Credito', 'Credito'),
               ('Debito', 'Debito'),
               ('Efectivo', 'Efectivo'),
               ('JUNAEB', 'JUNAEB'))
    credito = forms.BooleanField(
        label='credito',
        required=False,
        initial=False
    )
    efectivo = forms.BooleanField(
        label='efectivo',
        required=False,
        initial=True
    )
    debito = forms.BooleanField(
        label='debito',
        required=False,
        initial=False
    )
    junaeb = forms.BooleanField(
        label='JUNAEB',
        required=False,
        initial=False
    )
    hora_apertura = forms.CharField(label="hora_apertura", widget=forms.TextInput(attrs={'class': 'validate'}))
    hora_clausura = forms.CharField(label="hora_clausura", widget=forms.TextInput(attrs={'class': 'validate'}))


class AlumnoForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value=True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class': 'validate'}))
    file = forms.FileField()


class ProductoForm(forms.Form):
    nombre = forms.CharField(label="nombre",
                             widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'pizza'}))
    descripcion = forms.CharField(label="descripcion", widget=forms.Textarea)
    precio = forms.IntegerField(label="precio")
    stock = forms.IntegerField(label="stock")
    file = forms.FileField()


class EditarVendedor(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class': 'validate'}))

    hora_apertura = forms.CharField(label="hora_apertura", widget=forms.TextInput(attrs={'class': 'validate'}))
    hora_clausura = forms.CharField(label="hora_clausura", widget=forms.TextInput(attrs={'class': 'validate'}))

    credito = forms.BooleanField(
        label='credito',
        required=False,
        initial=False
    )
    efectivo = forms.BooleanField(
        label='efectivo',
        required=False,
        initial=True
    )
    debito = forms.BooleanField(
        label='debito',
        required=False,
        initial=False
    )
    junaeb = forms.BooleanField(
        label='JUNAEB',
        required=False,
        initial=False
    )

    foto = forms.ImageField()

    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value=True))
