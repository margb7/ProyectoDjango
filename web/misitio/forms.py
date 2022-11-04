from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    
    class Meta:

        model = Cliente
        fields = ['dni', 'nombre', 'alta', 'direccion', 'movil']
