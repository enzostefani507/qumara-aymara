from perfil.models import Usuario
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from . import forms
from blog.models import Post
class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = forms.LoginForm
    template_name = 'perfil/login.html'
    success_url = reverse_lazy('')

class miPerfil(LoginRequiredMixin,DetailView):    
    template_name = 'perfil/perfil.html'
    model = Usuario
    login_url = 'login'

    def get_queryset(self, *args, **kwargs):
        return Usuario.objects.filter(pk=self.request.user.id)


class miFavoritos(LoginRequiredMixin,ListView):
    template_name = 'perfil/post_favoritos.html'
    model = Post
    login_url = 'login'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        usuario = Usuario.objects.filter(pk=self.request.user.id)[0]
        context['object_list'] = usuario.post_favoritos
        return context
        
