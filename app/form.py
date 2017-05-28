from django import forms

from .models import VendedorAmbulante
from .models import VendedorFijo
from .models import Alumno

#class VendedorAmbulanteForm(forms.ModelForm):

##       model = VendedorAmbulante
  #      fields = ('vendedor',)

class VendedorFijoForm(forms.Form):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={'class':'validate'}))
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class':'validate'}))
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput(attrs={'class':'validate'}))
    email = forms.CharField(label="email", widget=forms.EmailInput(attrs={'class':'validate'}))
    CHOICES=(('Credito','Credito'),
             ('Debito','Debito'),
             ('Efectivo','Efectivo'),
             ('JUNAEB','JUNAEB'))
    pago = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
    )
    hora_apertura = forms.CharField(label="hora_apertura", widget=forms.TextInput(attrs={'class':'validate'}))
    hora_clausura = forms.CharField(label="hora_clausura", widget=forms.TextInput(attrs={'class':'validate'}))

#class AlumnoForm(forms.ModelForm):

#    class Meta:
 #       model = Alumno
  #      fields = ('email', 'password',)