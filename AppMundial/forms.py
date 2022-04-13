from django import forms
    

class JugadoresFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    posicion=forms.CharField(max_length=30)
    
class GrupoFormulario(forms.Form):
    
    letra_grupo= forms.CharField(max_length=10)
    pais_equipo= forms.CharField(max_length=15)    
    clasificacion=forms.IntegerField()