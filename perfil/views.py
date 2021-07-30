from django import forms
from perfil.models import Usuario
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from perfil.forms import SignInForm,LoginForm
from django.shortcuts import  render, redirect
from blog.models import Post

def register_request(request):
	if request.method == "POST":
		form = SignInForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignInForm()
	return render (request=request, template_name="perfil/registro.html", context={"form":form})

class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = LoginForm
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
        
