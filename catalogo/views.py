from django.views.generic import ListView, DetailView
from .models import Producto
from blog.models import Post

class ProductosList(ListView):
    model = Producto
    template_name = 'catalogo/catalogo_list.html'
    context_object_name = 'productos_list'
    paginate_by =  8

    def get_context_data(self, **kwargs):
        context = super(ProductosList, self).get_context_data(**kwargs)
        context['title'] = "Qumara Aymara - Catalogo"
        return context

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'catalogo/detalle.html'
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoDetail, self).get_context_data(**kwargs)
        producto = self.object.id
        post = Post.objects.filter(ingredientes = producto)
        context['title'] = "Qumara Aymara - Producto"
        context['util'] = post
        return context