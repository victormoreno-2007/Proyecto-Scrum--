import os

#Funcion  limpiar consola 
def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Funcion Intereactiva para el usuario enter continuar
def enterParaContinuar(mensaje: str = "Enter para continuar"):
    input(mensaje)