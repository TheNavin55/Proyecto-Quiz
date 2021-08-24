from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jugar(request):
    return render(request, 'juego.html',{})

def login(request):
    return render(request, 'login.html',{})

def create(request):
    return render(request, 'create.html',{})

def nosotros(request):
    return render(request, 'nosotros.html',{})