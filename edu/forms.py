from django import forms
from .models import Autor, Editora, Livro

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
