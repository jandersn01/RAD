from datetime import date

from django.test import TestCase
from edu.models import Editora, Livro, Curso

class LivroModelTest(TestCase):
    
    def setUp(self):
        self.editora = Editora.objects.create(nome="Editora Teste")
        self.livro = Livro.objects.create(
            titulo="Testando o modelo Livro",  
            editora=self.editora,
            publicacao=date(2024, 1, 1),
            ISBN="1234567890123",
            preco=29.99
        )

    def test_livro_creation(self):
        self.assertEqual(self.livro.titulo, "Testando o modelo Livro")
        self.assertEqual(self.livro.editora, self.editora)
        self.assertEqual(self.livro.publicacao, date(2024, 1, 1))
        self.assertEqual(self.livro.ISBN, "1234567890123")
        self.assertEqual(self.livro.preco, 29.99)

    def test_livro_str(self):
        self.assertEqual(str(self.livro), "Testando o modelo Livro")

    def test_campo_titulo_max_length(self):
        max_length = self.livro._meta.get_field('titulo').max_length
        self.assertEqual(max_length, 100)

    class CursoModelTest(TestCase):

        def setUp(self):
            self.curso = Curso.objects.create(
                nome = "Testando o modelo Curso"
            )

        def test_curso_creation(self):
            self.assertEqual(self.curso.nome, "Testando o modelo Curso")
            self.assertIsInstance(self.curso, Curso)


        def test_curso_str(self):
            self.assertEqual(str(self.curso), "Testando o modelo Curso")