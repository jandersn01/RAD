
from django.urls import reverse
from edu.models import Autor, Editora, Livro, Curso, Aluno
from rest_framework.test import APIClient, APITestCase

class ApiLivroTest(APITestCase):
    def setUp(self):
        self.cliente = APIClient()
        self.editora = Editora.objects.create(nome="Editora Teste")
        self.livro = Livro.objects.create(
            titulo="Livro Teste",
            ISBN="1234567890123",
            publicacao="2024-01-01",
            preco=29.99,
            editora=self.editora
        )
        self.autor = Autor.objects.create(nome="Autor Teste")
        self.autor.livro.add(self.livro)

    def test_list_livros_api(self):
        response = self.cliente.get("/edu/api/livros/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['titulo'], "Livro Teste")

    def test_retrieve_livro_api(self):
        response = self.cliente.get(f"/edu/api/livros/{self.livro.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['titulo'], "Livro Teste")

    def test_create_livro_api(self):
        data = {
            "titulo": "Novo Livro Teste",
            "ISBN": "9876543210123",
            "publicacao": "2024-02-01",
            "preco": 39.99,
            "editora": self.editora.id,
            "autor": [self.autor.id]
        }
        response = self.cliente.post("/edu/api/livros/", data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Livro.objects.count(), 2)
        self.assertEqual(Livro.objects.last().titulo, "Novo Livro Teste")
