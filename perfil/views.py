from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
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
    model = User

    def get_queryset(self, *args, **kwargs):
        return User.objects.filter(pk=self.request.user.id)