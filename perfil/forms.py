from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({'class' : 'form-control','placeholder' : "Usuario", 'type' : 'text','autofocus': 'autofocus'})
        self.fields["password"].widget.attrs.update({'class' : 'form-control','placeholder' : "Contraseña", 'type' : 'text'})