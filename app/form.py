from django import forms

from .models import VendedorAmbulante
from .models import VendedorFijo
from .models import Alumno

class VendedorAmbulanteForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value = True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value = True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class':'validate'}))
    file = forms.FileField()
    CHOICES=(('Credito','Credito'),
             ('Debito','Debito'),
             ('Efectivo','Efectivo'),
             ('JUNAEB','JUNAEB'))
    pago = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
    )

class VendedorFijoForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value = True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value = True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class':'validate'}))
    file = forms.FileField()
    CHOICES=(('Credito','Credito'),
             ('Debito','Debito'),
             ('Efectivo','Efectivo'),
             ('JUNAEB','JUNAEB'))
    credito = forms.BooleanField(
        label='Credito',
        initial=True
    )
    efectivo = forms.BooleanField(
        label='Efectivo',
        initial=True
    )
    debito = forms.BooleanField(
        label='Debito',
        initial=True
    )
    junaeb = forms.BooleanField(
        label='JUNAEB',
        initial=True
    )
    hora_apertura = forms.CharField(label="hora_apertura", widget=forms.TextInput(attrs={'class':'validate'}))
    hora_clausura = forms.CharField(label="hora_clausura", widget=forms.TextInput(attrs={'class':'validate'}))

class AlumnoForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(render_value = True))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(render_value = True))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class':'validate'}))
    file = forms.FileField()