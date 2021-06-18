from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto

class ProductosList(ListView):
    model = Producto
    template_name = 'catalogo/catalogo_list.html'