from apps.appPrincipal.models import Pregunta
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def jugar(request):
    listaIds = Pregunta.objects.filter(descripcion__isnull = False).values_list('id', flat = True)
    listaIdsRandom = random.sample(list(listaIds), 4)
    preguntas = Pregunta.objects.filter(id__in = listaIdsRandom)
    return render(request, 'jugar.html',{'preguntas': preguntas})

def login(request):
    return render(request, 'login.html',{})

def create(request):
    return render(request, 'create.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})

def menu(request):
    return render(request, 'menu.html',{})

def resultados(request):
    return render(request, 'resultados.html',{})