from django.contrib import admin
from .models import Opinion

class OpinionAdmin(admin.ModelAdmin):
    list_display = ["id","autor","contenido","fecha_creacion"]
    list_editable = ["autor","contenido"]

admin.site.register(Opinion,OpinionAdmin)