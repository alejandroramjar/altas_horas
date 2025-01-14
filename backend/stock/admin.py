from django.contrib import admin
from .models import Mercancia

@admin.register(Mercancia)
class MercanciaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_unitario', 'stock']  # Campos a mostrar en la lista del admin
    search_fields = ['nombre', 'qr_number']  # Campos para buscar

#admin.site.register(Mercancia, MercanciaAdmin)