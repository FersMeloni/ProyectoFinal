from django.urls import path
from AppMundial import views



urlpatterns = [
    
    path('', views.inicio,name="Inicio"),
    path('grupo/', views.grupo, name="Grupos"),
    path('sede/',views.sede, name="Sedes"),
    path('jugador/',views.jugadores,name="Jugadores"),
    path('jugador/',views.jugador,name="Jugadores"),
    # path('jugadorFormulario/',views.jugador,name="JugadorFormulario"),
    # path('busquedaEquipo/',views.busquedaEquipo, name="BusquedaEquipo"),
    # path('busquedaJugador/',views.busquedaJugador, name="")
    path('buscar/',views.buscar)
    
]