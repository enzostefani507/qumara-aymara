from django import forms

class ComentarioForm(forms.Form):
    nombre = forms.CharField()
    mensaje = forms.CharField(
        widget = forms.Textarea(
            attrs={            
                'style': 'height: 6em;'
                }
        )
    )