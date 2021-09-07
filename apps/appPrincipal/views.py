from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login as logear, logout as salir
from django.contrib.auth.decorators import login_required
import random

from .models import Pregunta, Juego, Juega
from .forms import NuevoUsuarioForm

# Create your views here.

@login_required(login_url='login')
def jugar(request):
    context = {}
    listaIds = Pregunta.objects.filter(descripcion__isnull = False).values_list('id', flat = True)
    listaIdsRandom = random.sample(list(listaIds), 4)
    preguntasRandom = Pregunta.objects.filter(id__in = listaIdsRandom).values()
    preguntas = []
    for item in preguntasRandom:
        pregunta = {}
        pregunta['id'] = item['id']
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

@login_required(login_url='login')
def resultados(request):
    if request.method == 'POST':
        print('esto es un POST')
        context = {}
        usuario = get_user_model()
        nombre = request.user
        aciertos = 0
        porcentaje = 0
        respuestas = [request.POST.get('q_answer1'), request.POST.get('q_answer2'),
            request.POST.get('q_answer3'), request.POST.get('q_answer4')]
        idPreguntas = [
            request.POST.get('id1'), request.POST.get('id2'),
            request.POST.get('id3'), request.POST.get('id4')
        ]
        print(idPreguntas)
        preguntas = list(Pregunta.objects.filter(id__in = idPreguntas))
        for respuesta in respuestas:
            if respuesta == 'True':
                aciertos += 1
        porcentaje = aciertos * 25
        juegoActual = Juego(
            puntaje = porcentaje
        )
        juegoActual.save()
        print('guardando objectos juega...')
        i = 0
        print(preguntas)
        for pregunta in preguntas:
            print('guardando usuario ' + str(i))
            Juega.objects.create(
                idParticipante = usuario,
                idJuego = juegoActual,
                idPregunta = pregunta,
                correcto = bool(respuestas[i])
            )
            print('deberia haberse creado un objecto')
            i += 1
        print('estoy despues del for')
        context['participante'] =  nombre
        context['aciertos'] = aciertos
        context['porcentaje'] = porcentaje
        return render(request, 'resultados.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('menu')
    else:
        if request.method == 'POST':
            print('Esto es un post')
            nombreUsuario = request.POST.get('username')
            print(nombreUsuario)
            password = request.POST.get('password')
            usuario = authenticate(request, username = nombreUsuario, password = password)
            print('Valiadando usuario...')
            if usuario is not None:
                print('Usuario valido')
                logear(request, usuario)
                return redirect('menu')
            else:
                print('Usuario invalido')
                messages.info(request, 'Nombre de usuario o contraseña no válido.')
                return render(request, 'login.html',{})
        return render(request, 'login.html',{})

#@login_required(login_url='login')
def logout(request):
    salir(request)
    return redirect('login')


def create(request):
    if request.user.is_authenticated:
        return redirect('menu')
    else:
        if request.method == 'POST':
            print('esto es un POST')
            form = NuevoUsuarioForm(request.POST)
            if form.is_valid():
                print('Nuevo usuario valido. Guardando...')
                form.save()
                #usuario = form.cleaned_data.get('username')
                #mensajes.success(request, 'La cuenta ' + usuario + ' fue creada exitosamente.')
                print('redirigiendo a login...')
                return redirect('login')
            else:
                messages.info(request, 'Nombre de usuario o contraseña no válido.')
                print(form.errors)
        form = NuevoUsuarioForm()
        context = {}
        context['form'] = form
        return render(request, 'create.html', context)

@login_required(login_url='login')
def nosotros(request):
    return render(request, 'nosotros.html',{})

@login_required(login_url='login')
def menu(request):
    return render(request, 'menu.html',{})