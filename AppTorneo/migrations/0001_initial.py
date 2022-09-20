# Generated by Django 4.1 on 2022-09-14 00:19

import AppTorneo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desequipo', models.CharField(max_length=100)),
                ('pj', models.IntegerField(default='0')),
                ('pg', models.IntegerField(default='0')),
                ('pp', models.IntegerField(default='0')),
                ('fktorneo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desfecha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomjugador', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('categoria', models.CharField(max_length=50)),
                ('cedula', models.IntegerField()),
                ('puntos', models.IntegerField(default='0')),
                ('fkequipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desresultado', models.CharField(max_length=50)),
                ('desres', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametorneo', models.CharField(max_length=50)),
                ('destorneo', models.CharField(max_length=140)),
                ('estado', models.CharField(max_length=30)),
                ('valor_torneo', models.IntegerField()),
                ('categoria', models.CharField(max_length=200)),
                ('fkfecha', models.DateField(verbose_name=AppTorneo.models.fecha)),
            ],
        ),
    ]
