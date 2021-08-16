from django import forms
from django.core.mail.message import EmailMultiAlternatives
from perfil.models import Usuario
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from perfil.forms import SignInForm, LoginForm
from django.shortcuts import render
from blog.models import Post
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

UserModel = get_user_model()

def register_request(request):
    if request.method == 'GET':
        form = SignInForm()
        return render(request, 'perfil/registro.html',{'form': form,'title':'Q\'umara Aymara - Registro'})
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Q\'umara Aymara - Activa tu cuenta!'
            html_message = render_to_string(
                'perfil/correo.html', 
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                mail_subject, html_message, to=[to_email]
            )
            email.attach_alternative(html_message,"text/html")
            email.send()
            return render (request, 'perfil/revisa_email.html', {'form': form,'title':'Q\'umara Aymara - Confirma tu email'})
        else:
            form = SignInForm(request.POST)
        return render(request, 'perfil/registro.html', {'form': form,'title':'Q\'umara Aymara - Registro'})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request,'perfil/cuenta_activada.html',{'title':'Q\'umara Aymara - Cuenta activada'})
    else:
        return render(request,'perfil/link_active_invalido.html',{'title':'Q\'umara Aymara - Error'})

class LogoutUsuario(LogoutView):
    success_url = 'home'

class LoginUsuario(LoginView):
    form_class = LoginForm
    template_name = 'perfil/login.html'
    success_url = reverse_lazy('')
    
    def get_context_data(self, **kwargs):
        context = super(LoginUsuario, self).get_context_data(**kwargs)
        context['title'] = 'Q\'umara Aymara - Iniciar Sesión'
        return context


class miPerfil(LoginRequiredMixin, DetailView):
    template_name = 'perfil/perfil.html'
    model = Usuario
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(miPerfil, self).get_context_data(**kwargs)
        context['title'] = 'Q\'umara Aymara - Mi Perfil'
        return context


    def get_queryset(self, *args, **kwargs):
        return Usuario.objects.filter(pk=self.request.user.id)


class miFavoritos(LoginRequiredMixin, ListView):
    template_name = 'perfil/post_favoritos.html'
    model = Post
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(miFavoritos,self).get_context_data(**kwargs)
        usuario = Usuario.objects.filter(pk=self.request.user.id)[0]
        context['object_list'] = usuario.post_favoritos
        context['title'] = 'Q\'umara Aymara - Favoritos'
        return context
