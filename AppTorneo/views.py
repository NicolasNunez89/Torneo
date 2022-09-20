from django.shortcuts import render, HttpResponse
from django.http.request import QueryDict
from django.http import HttpResponse
from AppTorneo.forms import CargaEquipoFormulario,CargaJugardorFormulario,CargaResultadoFormulario,CargaTorneoFormulario
from AppTorneo.models import equipo,fecha, jugador
# Create your views here.

def inicio(request):
    
      return render(request, "inicio.html")