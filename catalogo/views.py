from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


class ProductosList(ListView):
    model = Producto
    template_name = 'catalogo/catalogo_list.html'
    context_object_name = 'productos_list'
    paginate_by =  8

    def get_context_data(self, **kwargs):
        context = super(ProductosList, self).get_context_data(**kwargs)
        context['title'] = "Qumara Aymara - Catalogo"
        return context
