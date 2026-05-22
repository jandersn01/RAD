from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'edu'

urlpatterns = [
    path("autores/create/", views.create_autor, name="create_autor"),
    path("autores/", views.list_autores, name="list_autores"),  
    path("autores/update/<int:autor_id>/", views.update_autor, name="update_autor"),
    path("autores/delete/<int:autor_id>/", views.delete_autor, name="delete_autor"),
    path("editoras/create/", views.create_editora, name="create_editora"),
    path("editoras/", views.list_editoras, name="list_editoras"),   
    path("editoras/update/<int:editora_id>/", views.update_editora, name="update_editora"),
    path("editoras/delete/<int:editora_id>/", views.delete_editora, name="delete_editora"),
    path("livros/create/", views.create_livro, name="create_livro"),
    path("livros/update/<int:livro_id>/", views.update_livro, name="update_livro"),
    path("livros/delete/<int:livro_id>/", views.delete_livro, name="delete_livro"),
    path("livros/", views.list_livros_paginator, name="list_livros_paginator")    
]