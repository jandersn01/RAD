from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'blog'

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("eco/<str:texto>/", views.eco, name="eco"),
    path("info/", views.info, name="info"),
    path("praticando_templates/<str:nome>/", views.praticando_templates, name="praticando_templates"),
    path("contato/<str:telefone>/", views.contato, name="contato"),
    path("", views.home, name="home"),
]