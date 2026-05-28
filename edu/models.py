from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    livro = models.ManyToManyField("Livro", related_name="autores")
    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    publicacao = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    editora = models.ForeignKey("Editora", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.titulo} ({self.ISBN})"


class Curso(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
