from django import forms
from .models import Autor, Editora, Livro, Curso, Aluno

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nome", "livro"]

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ["nome"]

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ["titulo", "ISBN", "publicacao", "preco", "editora"]

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        exclude = ["id"]

class AlunoForm (forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ["id"]
