from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class resultado(models.Model):
    desresultado = models.CharField(max_length=50)
    desres = models.CharField(blank=False, max_length=50)

class fecha(models.Model):
    desfecha = models.CharField(blank=False, max_length=50)

class torneo(models.Model):
    nametorneo = models.CharField(max_length=50)
    #fkusr = models.ForeignKey(User)
    destorneo = models.CharField(max_length=140)
    estado = models.CharField(max_length=30)
    valor_torneo = models.IntegerField()
    categoria = models.CharField(max_length=200)
    fkfecha = models.DateField(fecha)
    def __unicode__(self):
    		return self.nametorneo

class equipo(models.Model):
	desequipo = models.CharField(blank=False, max_length=100)
	pj = models.IntegerField(blank=False, default="0")
	pg = models.IntegerField(blank=False, default="0")
	pp = models.IntegerField(blank=False, default="0")
	fktorneo = models.IntegerField()
	def __unicode__(self):
     		return '%s - %s' %(self.desequipo,self.fktorneo)

class jugador(models.Model):
    nomjugador = models.CharField(blank=False, max_length=50)
    sexo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    categoria = models.CharField(max_length=50)
    cedula = models.IntegerField()
    puntos = models.IntegerField(default="0")
    fkequipo = models.IntegerField()
