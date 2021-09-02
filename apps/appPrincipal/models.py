from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, DateField, EmailField, IntegerField, TextField, TimeField

# Create your models here.
class Participante(models.Model):
    usuario = CharField("Nombre con el que el usuario se identifica en el juego", max_length = 50)
    contrasena = CharField("Contraseña del usuario", max_length = 15)
    email = EmailField("Email del usuario para contacto en caso de perdida de contraseña", max_length = 75)

class Pregunta(models.Model):
    descripcion = TextField("Texto que representa la pregunta propiamente dicha")
    categoria = CharField("Categoria a la que pertenece la pregunta", max_length = 25)
    respuestaCorrecta = TextField("Respuesta correcta a la pregunta")
    incorrecta1 = TextField("Una respuesta incorrecta a la pregunta")
    incorrecta2 = TextField("Una respuesta incorrecta a la pregunta")
    incorrecta3 = TextField("Una respuesta incorrecta a la pregunta")

    def __str__(self) -> str:
        return self.descripcion

class Juego(models.Model):
    fecha = DateField("Fecha en la que se creo el juego", auto_now_add = True)
    hora = TimeField("Hora en la que se creo el juego", auto_now_add = True)
    puntaje = IntegerField("Puntaje obtenido por el jugador", default = 0)

class Juega(models.Model):
    idParticipante = models.ForeignKey(Participante, on_delete = models.CASCADE)
    idJuego = models.ForeignKey(Juego, on_delete = models.CASCADE)
    idPregunta = models.ForeignKey(Pregunta, on_delete = DO_NOTHING)
    correcto = models.BooleanField(default = False)

    class Meta:
        unique_together = (("idParticipante", "idJuego", "idPregunta"),)
