from rest_framework import viewsets
from edu.models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serialazer_class = LivroSerializer