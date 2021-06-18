from django.conf.urls import url
from . import views

urlpatterns = [
    url('/catalogo', views.catalogo, name='catalogo'),
]