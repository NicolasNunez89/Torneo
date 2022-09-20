from django.urls import path

from AppTorneo import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio")
]

