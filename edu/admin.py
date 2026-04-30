from django.contrib import admin
from .models import Autor, Editora, Livro

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "ISBN", "publicacao", "preco", "editora")
    search_fields = ("titulo", "ISBN")
    list_filter = ("publicacao", "editora")
