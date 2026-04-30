import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
def praticando_templates(request, nome:str):
    context = {
        "nome": nome,
        "data": datetime.date(2026, 4, 15),
        "is_logged_in": True,
        "produtos": [
            {"nome": "Produto 1", "preco": 10.99},
            {"nome": "Produto 2", "preco": 20.50},
            {"nome": "Produto 3", "preco": 15.75},
        ]
    }
    return render(request, "praticando_templates.html", context)

def home(request):
    return render(request, "home.html")

def contato(request, telefone:str):
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return render(request, "contato.html", {"telefone": telefone_formatado})

def welcome(request):
    return HttpResponse("Bem vindo ao meu blog!")

def eco(request, texto:str):
    return HttpResponse(f'Você digitou : {texto}')

def info(request):
    data = {
     "disciplina": "RAD",
     "framework": "Django",
     "semestre": "2025.2"
  }
    return JsonResponse(data)

