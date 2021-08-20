from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    texto={'mensaje_texto':'Este es mi primer mensaje :)'}
    return render(request, 'index.html',texto)

def login(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'login.html',{})

def create(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'create.html',{})

def nosotros(request):
    #return HttpResponse("Hola estoy en la pagina de contacto")
    return render(request, 'nosotros.html',{})