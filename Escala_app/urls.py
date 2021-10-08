from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path("home_medico/", home.medico, name= "home_medico"),
    path("medico/", cadastrar_medicos, name= "medico"),
    path("lista_medico/", lista_medico, name= "lista_medico"),
    path("alterar_medico/", atualizar_medico, name='alterar_medico'),

    path("home_posto/", home.posto, name= "home_posto"),
    path("posto/", cadastrar_posto, name= "posto"),
    path("lista_posto/", lista_posto, name= "lista_posto"),
    path("alterar_posto/", atualizar_posto, name='alterar_posto'),

    path("home_folga/", home.folga, name= "home_folga"),

    path("home_escala/", home.escala, name= "home_escala"),
]