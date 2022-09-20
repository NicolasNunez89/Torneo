from django import forms


class CargaJugardorFormulario(forms.Form):
    nomjugador = forms.CharField(max_length=50)
    sexo = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField()
    categoria = forms.CharField(max_length=50)
    cedula = forms.IntegerField()
    puntos = forms.IntegerField()
    fkequipo = forms.IntegerField()


class CargaEquipoFormulario(forms.Form):
    desequipo = forms.CharField()
    pj = forms.IntegerField()
    pg = forms.IntegerField()
    pp = forms.IntegerField()
    fktorneo = forms.IntegerField()


class CargaTorneoFormulario(forms.Form):
    nametorneo = forms.CharField(max_length=50)
    destorneo = forms.CharField(max_length=140)
    estado = forms.CharField(max_length=30)
    valor_torneo = forms.IntegerField()
    categoria = forms.CharField(max_length=200)
    fkfecha = forms.DateField()

class CargaResultadoFormulario(forms.Form):
    desresultado = forms.CharField(max_length=50)
    desres = forms.CharField(max_length=50)