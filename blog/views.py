from django.views.generic import ListView, DetailView
from .models import Post

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