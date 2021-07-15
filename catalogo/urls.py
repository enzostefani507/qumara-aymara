from django.urls import path
from .views import ProductoDetail,ProductosList

urlpatterns = [
    path('', ProductosList.as_view(), name='catalogo'),
    path('/<int:pk>', ProductoDetail.as_view(), name="producto_detalle")
]