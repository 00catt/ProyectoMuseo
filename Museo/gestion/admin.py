from django.contrib import admin
from .models import Cliente,Artista,Producto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Artista)
admin.site.register(Producto)