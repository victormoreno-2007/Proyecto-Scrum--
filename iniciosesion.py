import os
import json
import getpass
from recomendacion import menuRecomendaciones
from gestionCanciones import menuPlaylist


usuario = None


def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enterParaContinuar(Continuar="\nPresione ENTER para continuar\n -> "):
    input(Continuar)

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r',encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo de usuarios no existe. Creando uno nuevo...")
        return {}
    except json.JSONDecodeError:
        print("Error al leer el archivo de usuarios. puede ser que no exista ningun usuario aún.")
        return {}

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w',encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, indent=4)

def iniciar_sesion():
    usuarios = cargar_usuarios()
    if not usuarios:
        print('no hay usuarios registrados aun. por favor registre uno primero')
        return None

    print("\n--- Inicio de Sesión ---")
    usuario = input("Nombre identificativo del usuario: ").strip()
    contraseña = getpass.getpass("Contraseña: ").strip()
    
    if usuario in usuarios:
        user_data = usuarios[usuario] 
        if "contraseña" in user_data and user_data["contraseña"] == contraseña:
            print(f"¡Bienvenido, {usuario}!")
            enterParaContinuar()
            limpiarConsola()
            return usuario
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")
    
    enterParaContinuar()
    limpiarConsola()
    return None

def submenuPrincipal():
        print("\n=== Submenú Principal ===")
        print("1. Recomendación de cantantes")
        print("2. Agregar o crear playlists")
        print("3. Ver playlists")
        print("4. Cerrar sesión")

def crearPlaylist(usuario_actual):
    lista_canciones = []

    nombre_playlist = input('escriba el nombre de la nueva playlist\n')
    descripcion = input('escriba la descripcion de su playlist, si desea omitir presione enter\n')
    cantidad = int(input('digite la catidad de canciones que va a ingresar\n'))
        
    for i in range(cantidad):
        cancion = input('escriba el nombre de la cancion\n')
        lista_canciones.append(cancion)

    try:
        with open('usuarios.json', 'r',encoding='utf-8' ) as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = {}

    if 'playlists' not in usuarios[usuario_actual]:
        usuarios[usuario_actual]['playlists'] = {}

    usuarios[usuario_actual]['playlists'][nombre_playlist] = {
        'descripcion':descripcion,
        'canciones':lista_canciones
    }
    with open('usuarios.json', 'w',encoding='utf-8') as file:
        json.dump(usuarios , file, indent=4)

    print(f'su playlists {nombre_playlist} a sido creada exitosamente')
    enterParaContinuar()
    limpiarConsola()


def menu_playlists(usuario_actual):
    
    while True:
        submenuPrincipal()
        
        opcion = input("Seleccione una opción:\n -> ")
        
        if opcion == "1":
            menuRecomendaciones()

        elif opcion == "2":
            crearPlaylist(usuario_actual)

        elif opcion == "3":
            def vertodasplaylist():
                try:
                    with open('usuarios.json', 'r',encoding='utf-8') as file:
                        informacion = json.load(file)

                    for clave,nombre in informacion.items():
                        print(f'usuario: {clave}')
                        playlists = nombre.get('playlists', {})
                        if playlists:
                            print('playlist:')
                            for nom_playlist in playlists:
                                print(f'{nom_playlist}')

                        else:
                            print('aun no hay playlist registradas')
                except FileNotFoundError:
                    print('no se encontro el archivo usuarios.json')


            def verMisPlaylist(usuario):
                
                try:
                    with open('usuarios.json', 'r',encoding='utf-8' )as file:
                        informacion = json.load(file)

                    if usuario in informacion:
                        playlists = informacion[usuario].get('playlists', {})
                        if playlists:
                            print(f'playlists del usuario {usuario}')
                            for nombre, contenido in playlists.items():
                                print(f'{nombre}: {contenido["descripcion"]}')
                        else:
                            print('aun no tienes playlist')
                    else:
                        print('el usuario no existe')
                        
                except FileNotFoundError:
                    print('no se encontro el archivo usuarios.json')
            menu = '''
            1. ver todas la playlist
            2. ver mis playlist
            3. ingresar a una playlist
            4. salir'''
            
            while True:
                    print(menu)
                    try:
                        opcion = int(input('seleccione la accion a realizar\n'))
                        if opcion == 1:
                            vertodasplaylist()
                            enterParaContinuar()
                            limpiarConsola()
                        elif opcion == 2:
                            verMisPlaylist(usuario_actual)
                            enterParaContinuar()
                            limpiarConsola()
                        elif opcion == 3:
                            verMisPlaylist(usuario_actual)
                            if not verMisPlaylist(usuario_actual):
                                enterParaContinuar()
                                limpiarConsola()
                                continue
                            nombre_playlist = input("Escribe el nombre de la playlist que deseas gestionar:\n-> ")
                            menuPlaylist(usuario_actual, nombre_playlist)
                            enterParaContinuar()
                            limpiarConsola()
                        elif opcion == 4:
                            break
                        else:
                            print('opcion no valida')
                            enterParaContinuar()
                            limpiarConsola()
                    except ValueError:
                        print('error, verifique de nuevo')
                        enterParaContinuar()
                        limpiarConsola()
        elif opcion == "4":
            global usuario
            if usuario is not None:
                print('aun no hay sesion abierta')
                enterParaContinuar()
                limpiarConsola()
            else:
                print('secion cerrada')
                usuario = None
                enterParaContinuar()
                limpiarConsola()
                break
        
        else:
            print("Opción no válida. Intente nuevamente.")
            enterParaContinuar()
            limpiarConsola()
            

def menu_gestion_playlist(usuario_actual, nombre_playlist):
    usuarios = cargar_usuarios()
    playlist = usuarios[usuario_actual]["playlists"][nombre_playlist]

    while True:

        GestorPlaylist= f"""
            Gestionando playlist: {nombre_playlist}
                1. Ver canciones
                2. Agregar canción
                3. Eliminar canción
                4. Volver al menú de playlists
        """
        
        print(GestorPlaylist)
        opcion = input("Seleccione una opción:\n -> ")
        
        if opcion == "1":
            print(f"\n--- Canciones en '{nombre_playlist}' ---")
            if not playlist["canciones"]:
                print("Esta playlist está vacía.")
            else:
                for i, cancion in enumerate(playlist["canciones"], 1):
                    print(f"{i}. {cancion}")
            enterParaContinuar()
        
        elif opcion == "2":
            nueva_cancion = input("\nNombre de la canción a agregar: ")
            playlist["canciones"].append(nueva_cancion)
            guardar_usuarios(usuarios)
            print(f"'{nueva_cancion}' ha sido agregada a '{nombre_playlist}'!")
            enterParaContinuar()
        
        elif opcion == "3":
            if not playlist["canciones"]:
                print("No hay canciones para eliminar.")
                enterParaContinuar()
                continue
                
            print("\n--- Seleccione canción a eliminar ---")
            for i, cancion in enumerate(playlist["canciones"], 1):
                print(f"{i}. {cancion}")
            
            try:
                num = int(input("Número de canción a eliminar: "))
                if 1 <= num <= len(playlist["canciones"]):
                    cancion_eliminada = playlist["canciones"].pop(num-1)
                    guardar_usuarios(usuarios)
                    print(f"'{cancion_eliminada}' ha sido eliminada de '{nombre_playlist}'.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Por favor ingrese un número válido.")
            enterParaContinuarr()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
            enterParaContinuar()



