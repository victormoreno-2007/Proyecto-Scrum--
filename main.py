import os
from registro import registrarUsuario
from iniciosesion import iniciar_sesion, menu_playlists  


#Funcion  limpiar consola 
def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Funcion Intereactiva para el usuario enter continuar
def enterParaContinuar(mensaje: str = "Enter para continuar"):
    input(mensaje)

def menuPrincipal():
    print(
            '''
    █▀▄▀█ █░█ █▀ █ █▀▀ █░░ ▄▀█ █▄░█ █▀▄ █▀
    █░▀░█ █▄█ ▄█ █ █▄▄ █▄▄ █▀█ █░▀█ █▄▀ ▄█

    1. Iniciar sesion 
    2. Registrarse 
    '''

)
while True:
    try:
        menuPrincipal()
        opcion = int(input("Ingresa la opcion\n"))
        if opcion == 1:
            usuario_ingresado = iniciar_sesion()
            if usuario_ingresado:
                menu_playlists(usuario_ingresado)
                break
            else:
                print('inicio de sesion fallida, presione enter para continuar...')
        elif opcion == 2:
            registrarUsuario()
            break
        else:
            print('opcion invalida')
            enterParaContinuar()
            limpiarConsola()
    except ValueError:
        print('valor ingresado no es valido')
        enterParaContinuar()
        limpiarConsola()
