from rest_framework import serializers
from edu.models import Autor, Editora, Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Livro
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'