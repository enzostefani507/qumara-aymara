from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from . import forms

class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = forms.LoginForm
    template_name = 'perfil/login.html'
    success_url = reverse_lazy('')