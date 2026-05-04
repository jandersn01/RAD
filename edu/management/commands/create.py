from django.core.management.base import BaseCommand
from edu.models import Autor, Editora, Livro
from faker import Faker

class Command(BaseCommand):
    help = "Cria dados de teste para Autor, Editora e Livro"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Criar editoras
        editoras = []
        for _ in range(5):
            editora = Editora.objects.create(nome=fake.company())
            editoras.append(editora)

        # Criar livros
        livros = []
        for _ in range(20):
            livro = Livro.objects.create(
                titulo=fake.sentence(nb_words=4),
                ISBN=fake.isbn13(),
                publicacao=fake.date_this_decade(),
                preco=round(fake.random_number(digits=5) / 100, 2),
                editora=fake.random_element(editoras)
            )
            livros.append(livro)

        # Criar autores
        for _ in range(10):
            autor = Autor.objects.create(nome=fake.name())
            autor.livro.set(fake.random_elements(livros, length=3))
