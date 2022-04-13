from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

class Grupo(models.Model):
    
    letra_grupo= models.CharField(max_length=10)
    pais_equipo = models.CharField(max_length=15)
    clasificacion=models.IntegerField()
     

class Sede(models.Model):
    
    nombre_sede=models.CharField(max_length=30)
    aforo_sede=models.IntegerField()
    ciudad_sede=models.CharField(max_length=20)
    


class Jugador(models.Model):
    
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=30)
    
    # def __str__(self):
    #     return f"Nombre: {self.jugador_nombre} / Edad: {self.jugador_edad} / Posicion: {self.Jugador_posicion}"
    
