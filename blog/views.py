from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import RedirectView
from .models import Post
from perfil.models import Usuario
from django.contrib.auth.decorators import login_required

class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'post_list'
    paginate_by =  8

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['title'] = "Qumara Aymara - Blog"
        return context

class PostDetail(DetailView):
    template_name = 'post/detalle.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = Usuario.objects.get(id=self.request.user.id)
            post = Post.objects.get(id=self.object.id)
            if post in user.post_favoritos.all():
                context['en_favoritos'] = True
            else:
                context['en_favoritos'] = False
        context['title'] = "Qumara Aymara - Blog"
        return context

@login_required(login_url='/perfil/login')
def tratar_favorito(request,id):
    post = get_object_or_404(Post, id = id)
    user = Usuario.objects.get(id=request.user.id)
    if post in user.post_favoritos.all():
        user.post_favoritos.remove(post)
    else:
        user.post_favoritos.add(post)
    return redirect('detalle_post',id)
        