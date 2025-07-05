import re
import getpass
import datetime

def nombre(nombre:str):
    return nombre

def validar_correo(correo: str) -> bool:
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

def nombredeseado(nombredeseado:str):
    return nombredeseado

def contraseña():
    contraseña = getpass.getpass("Ingresa tu contraseña: ")
    return '*'*len(contraseña)

def fecha_hora():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

menu ='''1.nombre
2.validar correo
3.nombre deseado
4contraseña
5.fecha'''


while True:
    print(menu)
    opcion = int(input(' digite una opcion'))
    if opcion == 1:
        nombre1=input('escriba el nombre')
        nom=nombre(nombre1)
        print(f'su nombre es {nom}')
    elif opcion==2:
        correoes=input('escriba el correo')
        vali=validar_correo(correoes)
        print(f'su correo es {vali}')
    elif opcion ==3:
        nombredes=input('escriba su nombre deseado')
        nomb=nombredeseado(nombredes)
        print(f'su nombre deseado es {nomb}')
    elif opcion==4:
        cont=contraseña()
        print(f'su contraseña es {cont}')
    elif opcion == 5:
        fecha_hora()
       