from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    livro = models.ManyToManyField("Livro", related_name="autores")

class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    editora = models.ForeignKey("Editora", on_delete=models.CASCADE)


class Curso(models.Model):
    nome = models.CharField(max_length=50)

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
