from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .viewsets import LivroViewSet, AutorViewSet, EditoraViewset

router = SimpleRouter()
router.register(r'livros', LivroViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'editoras', EditoraViewset)

urlpatterns = [
    path('', include(router.urls))
]