from django import forms
from .models import Cliente


class ClienteLogin(forms.ModelForm):

    class Meta:

        model = Cliente
        fields = ["email", "password"]
