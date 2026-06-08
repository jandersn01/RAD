from django.test import TestCase
from django.urls import reverse
from edu.models import Autor, Editora, Livro, Curso, Aluno
from datetime import date

class ListLivrosViewTest(TestCase):
    def setUp(self):
        self.editora = Editora.objects.create(nome="Editora Teste")
        self.livro = Livro.objects.create(
            titulo="Livro Teste",
            ISBN="1234567890123",
            publicacao=date(2024, 1, 1),
            preco=29.99,
            editora=self.editora
        )
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.autor.livro.add(self.livro)

    def test_list_livros_view(self):
        url = reverse("edu:list_livros_paginator")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Livro Teste")