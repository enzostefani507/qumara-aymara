from django.views.generic import ListView, DetailView
from .models import Post, Comentario
from .forms import ComentarioForm

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
    form_class = ComentarioForm

    def post(self):
        self.object = self.get_object()
        form = self.get_form()
        self.success_url = '/post/%d' % self.object.id
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)