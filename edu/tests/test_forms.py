from django.test import TestCase
from django.urls import reverse
from edu.models import Autor, Editora, Livro, Curso, Aluno
from datetime import date

class LivroFormTest(TestCase):
    def test_livro_form(self):
        url = reverse("edu:create_livro")
        data = {
            "titulo": "Livro Teste",
            "ISBN": "1234567890123",
            "publicacao": date(2024, 1, 1),
            "preco": 29.99,
            "editora": Editora.objects.create(nome="Editora Teste").id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após criação
        self.assertTrue(Livro.objects.filter(titulo="Livro Teste").exists())