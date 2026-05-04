from django.shortcuts import render

from edu.forms import AutorForm, EditoraForm, LivroForm
from edu.models import Autor, Editora, Livro
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def create_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()
    return render(request, "./form_autor.html", {"form": form})

def list_autores(request):
    autores = Autor.objects.all()
    return render(request, "./list_autores.html", {"autores": autores})

def update_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm(instance=autor)
    return render(request, "./form_autor.html", {"form": form})

def delete_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == "POST":
        autor.delete()
    return render(request, "./delete_autor.html", {"autor": autor})


def create_editora(request):
    if request.method == "POST":
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
    else:        form = EditoraForm()
    return render(request, "./form_editora.html", {"form": form})

def list_editoras(request):
    editoras = Editora.objects.all()
    return render(request, "./list_editoras.html", {"editoras": editoras})

def update_editora(request, editora_id):
    editora = Editora.objects.get(id=editora_id)
    if request.method == "POST":
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
    else:
        form = EditoraForm(instance=editora)
    return render(request, "./form_editora.html", {"form": form})

def delete_editora(request, editora_id):
    editora = Editora.objects.get(id=editora_id)
    if request.method == "POST":
        editora.delete()
    return render(request, "./delete_editora.html", {"editora": editora})

def create_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LivroForm()
    return render(request, "./form_livro.html", {"form": form})

def update_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
    else:
        form = LivroForm(instance=livro)
    return render(request, "./form_livro.html", {"form": form})

def delete_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    if request.method == "POST":
        livro.delete()
    return render(request, "./delete_livro.html", {"livro": livro})

def list_livros_paginator(request):
    livro_list = Livro.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(livro_list, 5)
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)
    return render(request, "./list_livros_paginator.html", {"livros": livros})