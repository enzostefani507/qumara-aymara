from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls')),
    path('blog/',include('blog.urls')),
    path('',include('home.urls')),
]