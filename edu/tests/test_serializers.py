from django.test import TestCase
from edu.models import Editora, Livro, Curso
from datetime import date

class LivroSerializerTest(TestCase):
    def setUp(self):
        self.editora = Editora.objects.create(nome="Editora Teste")
        self.livro = Livro.objects.create(
            titulo="Testando o modelo Livro", 
            editora=self.editora,
            publicacao=date(2024, 1, 1),
            ISBN="1234567890123",
            preco=29.99
        )

    def test_livro_serializer(self):
        from edu.DRF.serializers import LivroSerializer
        serializer = LivroSerializer(instance=self.livro)
        data = serializer.data
        self.assertEqual(data['titulo'], "Testando o modelo Livro")
        self.assertEqual(data['editora'], self.editora.id)
        self.assertEqual(
                            data["publicacao"],"2024-01-01"
                )
        self.assertEqual(data['ISBN'], "1234567890123")
        self.assertEqual(float(data['preco']), 29.99)

    def test_serializer_with_invalid_data(self):
        from edu.DRF.serializers import LivroSerializer
        data = {
            "titulo": "",
            "editora": self.editora.id,
            "publicacao": "invalid",
            "ISBN": "invalid",
            "preco": "invalid"
        }
        serializer = LivroSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('titulo', serializer.errors)
        self.assertIn('editora', serializer.errors)
        self.assertIn('publicacao', serializer.errors)
        self.assertIn('ISBN', serializer.errors)
        self.assertIn('preco', serializer.errors)
