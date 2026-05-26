from django.contrib import admin
from .models import Autor, Editora, Livro, Curso, Aluno

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

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome")

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "curso")
    search_fields = ("nome", "curso")
    list_filter = ("curso")