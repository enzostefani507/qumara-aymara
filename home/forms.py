from django import forms
from django.forms import widgets
from .models import Opinion

class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinion

        fields = [
            'autor',
            'contenido',
        ]

        labels = {
            'autor':'Nombre',
            'contenido':'Texto',
        }

        widgets = {
            'autor' : forms.TextInput(attrs={'class':'form-control','size':'50px'}),
            'contenido' : forms.TextInput(attrs={'class':'form-control'}),
        }