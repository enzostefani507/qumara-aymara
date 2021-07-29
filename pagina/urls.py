from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo',include('catalogo.urls')),
    path('post',include('blog.urls')),
    path('perfil',include('perfil.urls')),
    path('',include('home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.views.static import serve


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]