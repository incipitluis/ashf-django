from django.contrib import admin
from .models import Articulos, Blog, PapersContent, Solicitudes

@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'year', 'estado', 'created_at')
    search_fields = ('titulo', 'autor')
    list_filter = ('estado', 'year')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'likes', 'created_at')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created_at',)

@admin.register(PapersContent)
class PapersContentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('content',)

@admin.register(Solicitudes)
class SolicitudesAdmin(admin.ModelAdmin):
    list_display = ('revisor', 'articulo', 'year', 'estado', 'created_at')
    search_fields = ('revisor', 'articulo')
    list_filter = ('estado', 'year')
