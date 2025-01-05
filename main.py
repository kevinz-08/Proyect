from datosJSON import *
from menuCrud.mensaje import *
from funciones import *
from module.regist import *
from module.login import *
equiposFutbol = abrirArchivo('equipos')

while True:
    print(saludo)
    opcion = getInt('8==)   ')
    match opcion:
        case 1:
            registrarse()
        case 2:
            login()
        case 3:
            pass
        case 4:
            print('chao')
            break
        case _:
            print('Opcion INvalida')