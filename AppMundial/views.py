from urllib import response
from xml.dom.pulldom import PROCESSING_INSTRUCTION
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse,request
    
from AppMundial.models import  Jugador,Sede,Grupo
from AppMundial.forms import  JugadoresFormulario, GrupoFormulario

# Create your views 

# def grupo (request):
    
#     grupo = Grupo(letra_grupo="A", pais_equipo="Argentina", clasificacion="1")
    
#     grupo.save()
    
#     documentoDeTexto = f"--->El Grupo: {grupo.letra_grupo} El pais: {grupo.pais_equipo}  clasificacion: {grupo.clasificacion}"
     
    
#     return HttpResponse(documentoDeTexto)

# def jugador (request):
    
#     jugador= Jugador(nombre="Juan Gomez",edad="32",posicion="Delantero")
    
#     jugador.save()
    
#     documentoDeTexto = f" Jugador:{jugador.nombre}, tiene{jugador.edad} Años y es{jugador.posicion}"

    
    # return HttpResponse(documentoDeTexto)


# def sede (request):
#     sede= Sede(nombre_sede="Estadio Áhmad Bin Ali", aforo_sede="40000",ciudad_sede="ciudad de Rayán")
#     sede.save()
    
#     documentoDeTexto= f"Sede: {sede.nombre_sede} Aforo: {sede.aforo_sede} Ciudad: {sede.ciudad_sede}"
    
#     return HttpResponse(documentoDeTexto)    
    


def inicio (request):
    return render (request, "AppMundial/inicio.html")

def grupo (request):
    return render (request, "AppMundial/grupos.html")


def sede (request):
    return render (request, "AppMundial/sedes.html")

def jugador(request):
    return render (request, "AppMundial/jugadores.html")


def jugadores(request):
    
    
    if request.method =='POST':
    
        
        miFormulario= JugadoresFormulario(request.POST)
        
        
        # print(miFormulario)
        
        if miFormulario.is_valid():
            
            informacion=miFormulario.cleaned_data
            
            # print(informacion)
            
        
            jugador= Jugador(nombre=informacion['nombre'], edad=informacion['edad'], posicion=informacion['posicion'])
            
            # print(jugador)    
        
            jugador.save()
        
            return render(request,"AppMundial/inicio.html")
        
    else:
        
        miFormulario= JugadoresFormulario()
        
    return render(request,"AppMundial/jugadores.html",{"miFormulario":miFormulario})


# def buscarjugadores(request):
    
#         return render (request, "AppMundial/busquedaEquipo.html")


def buscar(request):
    if request.GET["posicion"]:
        
        posicion=request.GET['posicion']
        jugador=Jugador.objects.filter(posicion__icontains=posicion)
        
        return render(request,"AppMundial/inicio.html",{"jugador":jugador,"posicion":posicion})
    
    else:
        respuesta= "no enviaste Datos"
    
    return HttpResponse(respuesta)

        
def buscar(request):
    
    if request.GET["posicion"]:
        
        posicion= request.GET['posicion']
        jugador= Jugador.objects.filter(posicion__icontains=posicion)
        edad= Jugador.objects.filter(posicion__icontains=posicion)

        return render(request, "AppMundial/resultadosbusqueda.html",{"jugador":jugador, "posicion":posicion,"Edad":edad})
    
    else:
        respuesta="No enviaste datos"
    
    return HttpResponse (respuesta)

        
    # respuesta= f"Estoy buscando el equipo clasificado Nro: { request.GET ['equipo']}"
    
    # return HttpResponse (respuesta)
      

# def leerJugadores(request):
#     jugadores =Jugador.objects.all()
#     contexto = {"jugadores":jugadores}
#     return render(request, "AppMundial/leerprofesores.html",contexto)

