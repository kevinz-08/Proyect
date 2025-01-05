from datosJSON import *
from funciones import *


sesion = abrirArchivo(RUTA_EQUIPOS)


def login():
    tarjeta = input("ingrese su tarjeta de identidad: ")
    for i in sesion['usuarios']["tarjeta"]:
        if tarjeta == i :
            eleccionEquipo = input("que equipo desea ver").lower()
        else: 
            print("usted necesita una cuenta para poder acceder al prgrama, por favor registrese.")