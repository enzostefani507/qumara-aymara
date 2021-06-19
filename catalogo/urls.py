from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.ProductosList.as_view(), name='catalogo'),
]