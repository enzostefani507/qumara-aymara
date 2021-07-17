from django.contrib import admin
from .models import Post, Categoria

class PostAdmin(admin.ModelAdmin):
    list_display = ["id","cateogoria","titulo","descripcion",]
    list_editable = ["titulo","descripcion"]
    search_fields = ["titulo"]
    actions = None

admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)