from apps.appPrincipal.models import Pregunta
from django.shortcuts import render
import random

# Create your views here.
def jugar(request):
    context = {}
    listaIds = Pregunta.objects.filter(descripcion__isnull = False).values_list('id', flat = True)
    listaIdsRandom = random.sample(list(listaIds), 4)
    preguntasRandom = Pregunta.objects.filter(id__in = listaIdsRandom).values()
    preguntas = []
    for item in preguntasRandom:
        pregunta = {}
        pregunta['descripcion'] = item['descripcion']
        pregunta['categoria'] = item['categoria']
        pregunta['respuestas'] = []
        rtas = [item['respuestaCorrecta'], item['incorrecta1'], item['incorrecta2'], item['incorrecta3']]
        rtas2 = list(enumerate(rtas, start=1))
        random.shuffle(rtas2)
        for valor in rtas2:
            respuesta = {}
            respuesta['texto'] = valor[1]
            if valor[0] != 1:
                respuesta['correcto'] = 'False'
            else:
                respuesta['correcto'] = 'True'
            pregunta['respuestas'].append(respuesta)
        preguntas.append(pregunta)
    context['preguntas'] = preguntas
    return render(request, 'jugar.html', context)

def login(request):
    return render(request, 'login.html',{})

def create(request):
    return render(request, 'create.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})

def menu(request):
    return render(request, 'menu.html',{})

def resultados(request):
    if request.method == 'POST':
        context = {}
        nombre = 'Nico'
        aciertos = 0
        porcentaje = 0
        respuestas = [request.POST.get('q_answer1'), request.POST.get('q_answer2'),
            request.POST.get('q_answer3'), request.POST.get('q_answer4')]
        for respuesta in respuestas:
            if respuesta == 'True':
                aciertos += 1
        porcentaje = aciertos * 25
        context['participante'] =  nombre
        context['aciertos'] = aciertos
        context['porcentaje'] = porcentaje
        return render(request, 'resultados.html', context)