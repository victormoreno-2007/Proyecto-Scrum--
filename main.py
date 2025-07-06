import os

#Funcion  limpiar consola 
def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
