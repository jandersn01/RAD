from django.shortcuts import render, redirect

from edu.forms import AutorForm, EditoraForm, LivroForm, CursoForm, AlunoForm
from edu.models import Autor, Editora, Livro, Curso, Aluno
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
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
    page = request.GET.get("page", 1)
    paginator = Paginator(autores, 5)
    try:
        autores = paginator.page(page)
    except PageNotAnInteger:
        autores = paginator.page(1)
    except EmptyPage:
        autores = paginator.page(paginator.num_pages)
    return render(request, "./list_autores.html", {"autores": autores})

@login_required
def update_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == "POST":
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm(instance=autor)
    return render(request, "./form_autor.html", {"form": form})

@login_required
def delete_autor(request, autor_id):
    autor = Autor.objects.get(id=autor_id)
    if request.method == "POST":
        autor.delete()
    return render(request, "./delete_autor.html", {"autor": autor})


@login_required
def create_editora(request):
    if request.method == "POST":
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
    else:        form = EditoraForm()
    return render(request, "./form_editora.html", {"form": form})


def list_editoras(request):
    editoras = Editora.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(editoras, 5)
    try:
        editoras = paginator.page(page)
    except PageNotAnInteger:
        editoras = paginator.page(1)
    except EmptyPage:        
        editoras = paginator.page(paginator.num_pages)
    return render(request, "./list_editoras.html", {"editoras": editoras})

@login_required
def update_editora(request, editora_id):
    editora = Editora.objects.get(id=editora_id)
    if request.method == "POST":
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
    else:
        form = EditoraForm(instance=editora)
    return render(request, "./form_editora.html", {"form": form})

@login_required
def delete_editora(request, editora_id):
    editora = Editora.objects.get(id=editora_id)
    if request.method == "POST":
        editora.delete()
    return render(request, "./delete_editora.html", {"editora": editora})

@login_required
def create_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LivroForm()
    return render(request, "./form_livro.html", {"form": form})

@login_required
def update_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    if request.method == "POST":
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
    else:
        form = LivroForm(instance=livro)
    return render(request, "./form_livro.html", {"form": form})

@login_required
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

@permission_required('edu.add_curso')
def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_cursos')
    else:
        form = CursoForm()
        return render(request, "./curso_form.html", {'form': form})
    
@permission_required('edu.view_curso')
def list_curso(request):
    cursos = Curso.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(cursos, 5)
    try:
        cursos = paginator.page(page)
    except PageNotAnInteger:
        cursos = paginator.page(1)
    except EmptyPage:
        cursos = paginator.page(page.num_pages)
    return render(request, './cursos.html', {'cursos': cursos})

@permission_required('edu:change_curso')
def update_curso(request, curso_id):
    curso = Curso.objects.get(id = curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST,instance=curso)
        if form.is_valid():
            form.save()
            return redirect('edu:list_cursos')
    else: 
        form = CursoForm(instance=curso)
        return render(request, './curso_form.html', {'form': form})
    
@permission_required('edu.delete_curso')
def delete_curso(request, id_curso):
    curso = get_object_or_404(Curso, id = id_curso)
    if request.method == 'POST':
        curso.delete()
        return redirect('edu:list_cursos')
    return redirect('edu:list_cursos')
    
@permission_required('edu.add_aluno')
def create_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu:list_alunos')
    else: 
        form = AlunoForm()
        return render(request, './aluno_form.html', {'form': form})


@permission_required('edu.view_aluno')
def list_aluno(request):
    alunos = Aluno.objects.all()
    page = request.GET.get('pages', 1)
    paginator = Paginator(alunos, 5)
    try:
        alunos = paginator.page(page)
    except EmptyPage:
        alunos = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        alunos = paginator.page(1)
    return render(request, './alunos.html', {'alunos': alunos})

@permission_required('edu.change_aluno')
def update_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id = id_aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect ('edu:list_alunos')
    else:
        form = AlunoForm()
        return render( request, './aluno_form.html', {'form': form})

@permission_required('edu.delete_aluno')
def delete_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id = id_aluno)
    if request.method == 'POST':
        aluno.delete()
        redirect('edu:list_alunos')
    return redirect ('edu:list_alunos')