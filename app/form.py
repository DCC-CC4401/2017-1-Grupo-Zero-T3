from django import forms

from .models import VendedorAmbulante
from .models import VendedorFijo
from .models import Alumno


class VendedorAmbulanteForm(forms.ModelForm):
    class Meta:
        model = VendedorAmbulante
        fields = ('email', 'password',)


class VendedorFijoForm(forms.ModelForm):
    class Meta:
        model = VendedorFijo
        fields = ('email', 'password',)


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('email', 'password',)
