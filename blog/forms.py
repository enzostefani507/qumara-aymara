from django import forms
from .models import Comentario

class ComentarioForm(forms.Form):
    class Meta:
        model = Comentario
    nombre = forms.CharField()
    mensaje = forms.CharField(
        widget = forms.Textarea(
            attrs={            
                'style': 'height: 6em;'
                }
        )
    )