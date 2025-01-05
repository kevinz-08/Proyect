from datosJSON import *

equipos = abrirArchivo(RUTA_EQUIPOS)


def registrarse():
    nombre = input('Digite su Nombre: ')
    tarjeta = input('Digite su T.i: ')
    dic = {
        'nombre': nombre,
        'tarjeta': tarjeta
    }
    
    equipos["usuarios"].append(dic)
    guardarArchivo(RUTA_EQUIPOS, equipos)

    
    
    