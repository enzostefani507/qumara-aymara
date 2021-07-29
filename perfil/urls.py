from django.urls import path
from . import views

urlpatterns = [
    path('/login', views.LoginUsuario.as_view(), name='login'),
    path('/logout', views.LogoutUsuario.as_view(), name="logout"),
    path('/mi_perfil<int:pk>', views.miPerfil.as_view(),name='perfil'),
    path('/post_favoritos', views.miFavoritos.as_view(),name='mis_favoritos')

]