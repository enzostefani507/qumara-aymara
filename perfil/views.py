from perfil.models import Usuario
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.detail import DetailView
from .models import Usuario
from django.urls import reverse_lazy
from . import forms

class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = forms.LoginForm
    template_name = 'perfil/login.html'
    success_url = reverse_lazy('')

class miPerfil(DetailView):    
    template_name = 'perfil/perfil.html'
    model = Usuario

    def get_queryset(self, *args, **kwargs):
        return Usuario.objects.filter(pk=self.request.user.id)