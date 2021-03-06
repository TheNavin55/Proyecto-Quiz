# Generated by Django 3.2.6 on 2021-08-24 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha en la que se creo el juego')),
                ('hora', models.TimeField(auto_now_add=True, verbose_name='Hora en la que se creo el juego')),
                ('puntaje', models.IntegerField(verbose_name='Puntaje obtenido por el jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50, verbose_name='Nombre con el que el usuario se identifica en el juego')),
                ('contrasena', models.CharField(max_length=15, verbose_name='Contraseña del usuario')),
                ('email', models.EmailField(max_length=75, verbose_name='Email del usuario para contacto en caso de perdida de contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Texto que representa la pregunta propiamente dicha')),
                ('respuestaCorrecta', models.TextField(verbose_name='Respuesta correcta a la pregunta')),
                ('incorrecta1', models.TextField(verbose_name='Una respuesta incorrecta a la pregunta')),
                ('incorrecta2', models.TextField(verbose_name='Una respuesta incorrecta a la pregunta')),
                ('incorrecta3', models.TextField(verbose_name='Una respuesta incorrecta a la pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Juega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idJuego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipal.juego')),
                ('idParticipante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipal.participante')),
                ('idPregunta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appPrincipal.pregunta')),
            ],
            options={
                'unique_together': {('idParticipante', 'idJuego')},
            },
        ),
    ]
