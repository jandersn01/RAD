from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def welcome(request):
    return HttpResponse("Bem vindo ao meu blog!")

def eco(request, texto:str):
    return HttpResponse(f'Você digitou : {texto}')
