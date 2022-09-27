from .models import *
from django.forms import ModelForm
from django import forms


class MensajeForm(ModelForm):
    class Meta:
        model= Mensaje
        fields = {
            'nombre',
            'email',
            'tipo_consulta',
            'mensaje',
        }
        widgets = {
            'nombre': forms.TextInput(),
            'email': forms.EmailInput(),
            'tipo_consulta': forms.Select,
            'mensaje': forms.Textarea,
        }
