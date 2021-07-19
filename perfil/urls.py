from django.urls import path
from . import views

urlpatterns = [
    path('/login', views.LoginUsuario.as_view(), name='login'),
    path('/logout', views.LogoutUsuario.as_view(), name="logout"),
]