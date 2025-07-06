import os
from registro import registrarUsuario

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

menuPrincipal()
opcion = int(input("Ingresa la opcion\n"))
if opcion == 1:
    pass
elif opcion == 2:
    if __name__ == "__main__":
        registrarUsuario()