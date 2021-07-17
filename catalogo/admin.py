from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id","en_stock_actual","nombre","marca","comentario"]
    list_editable = ["en_stock_actual","nombre","marca","comentario"]
    search_fields = ["nombre","marca"]
    list_filter = ["en_stock_actual","marca"]
    actions = None

admin.site.register(Producto, ProductoAdmin)