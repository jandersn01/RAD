from rest_framework import viewsets
from edu.models import Autor, Livro, Editora
from .serializers import AutorSerializer, LivroSerializer, EditoraSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class EditoraViewset(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer