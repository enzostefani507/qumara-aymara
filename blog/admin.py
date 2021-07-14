from django.contrib import admin
from .models import Comentario, Post, Categoria

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)