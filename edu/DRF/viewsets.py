from rest_framework import viewsets
from edu.models import Autor, Livro, Editora
from .serializers import AutorSerializer, LivroSerializer, EditoraSerializer
from rest_framework.permissions import DjangoModelPermissions

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [DjangoModelPermissions]

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [DjangoModelPermissions]

class EditoraViewset(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [DjangoModelPermissions]