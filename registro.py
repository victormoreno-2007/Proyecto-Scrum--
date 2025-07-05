import re
import getpass
import datetime
import json

def registrarUsuario():
    def nombreCompleto():
        nombre = input('por favor ingrese su nombre completo:\n')
        return nombre

    def validarCorreo():
        while True:
            correo = input('ingrese su correo\n')
            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(patron, correo):
                print('correo valido')
                return correo
            else:
                print('correo invalido, intentelo de nuevo')

    def nombreDeseado():
        nombredeseado=input('por favor ingrese el nombre con el cual quiere a\n')
        return nombredeseado

    def contraseñaUsuario():
        clave = getpass.getpass("Ingresa tu contraseña: \n")
        final = clave[-3:] if len(clave) >= 3 else clave
        print('Contraseña recibida:' + '*' * (len(clave) - len(final)) + final)
        return clave

    def fecha_hora():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    nombre = nombreCompleto()
    correo = validarCorreo()
    nombreUsuario = nombreDeseado()
    contraseña = contraseñaUsuario()
    fecha = fecha_hora()


    informacion = {
        'nombre':nombre,
        'correo':correo,
        'nombreUsuario': nombreUsuario,
        'contraseña':contraseña,
        'fecha':fecha
    }

    try:
        with open('usuario.json','r',encoding='utf-8') as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = []

    datos.append(informacion)

    with open('usuarios.json','w',encoding='utf-8') as file:
        json.dump(datos,file, indent=4, ensure_ascii=False)

    print('usuario registrado correctamente')

registrarUsuario()