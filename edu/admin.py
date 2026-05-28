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
class FaixaPrecoFilter(admin.SimpleListFilter):
    title = 'faixa de preço'
    parameter_name = "faixa_preco"
    
    def lookups(self, request, model_admin):
        return ( 
            ("baixo", "Até R$ 50"),
            ("medio", "De R$ 50 a R$ 100"),
            ("alto", "Acima de R$ 100"),
            )
    
    def queryset(self, request, queryset):
        if self.value() == "baixo":
            return queryset.filter(preco__lte=50)
        if self.value() == "medio":
            return queryset.filter(preco__gt=50, preco__lte=100)
        if self.value() == "alto":
            return queryset.filter(preco__gt=100)
        
        return self.queryset

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "ISBN", "publicacao", "preco", "editora")
    search_fields = ("titulo", "ISBN", "editora__nome")
    list_filter = ("publicacao", "editora", FaixaPrecoFilter)
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "curso")
    search_fields = ("nome", "curso__nome")
    list_filter = ("curso",)