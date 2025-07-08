import json
import getpass
from recomendacion import menuRecomendaciones
from gestionCanciones import pas
usuario = None


def ENTERContinuar(Continuar="\nPresione ENTER para continuar\n -> "):
    input(Continuar)

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo de usuarios no existe. Creando uno nuevo...")
        return {}
    except json.JSONDecodeError:
        print("Error al leer el archivo de usuarios. Verifica el formato.")
        return {}

def guardar_usuarios(usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    print("\n--- Inicio de Sesión ---")
    usuario = input("Nombre identificativo del usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"¡Bienvenido, {usuario}!")
        return usuario
    else:
        print("Usuario o contraseña incorrectos.")
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
        with open('usuarios.json', 'r' ) as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        usuarios = {}

    if 'playlists' not in usuarios[usuario_actual]:
        usuarios[usuario_actual]['playlists'] = {}

    usuarios[usuario_actual]['playlists'][nombre_playlist] = {
        'descripcion':descripcion,
        'canciones':lista_canciones
    }
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios , file, indent=4)

    print(f'su playlists {nombre_playlist} a sido creada exitosamente')


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
                    with open('usuarios.json', 'r') as file:
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
                    with open('usuarios.json', 'r' )as file:
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
                        elif opcion == 2:
                            verMisPlaylist(usuario_actual)
                        elif opcion == 3:
                            pass
                        elif opcion == 4:
                            break
                        else:
                            print('opcion no valida')
                    except ValueError:
                        print('error, verifique de nuevo')
        elif opcion == "4":
            global usuario
            if usuario is not None:
                print('aun no hay sesion abierta')
            else:
                print('secion cerrada')
                usuario = None
                break
        
        else:
            print("Opción no válida. Intente nuevamente.")
            ENTERContinuar()
            

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
            ENTERContinuar()
        
        elif opcion == "2":
            nueva_cancion = input("\nNombre de la canción a agregar: ")
            playlist["canciones"].append(nueva_cancion)
            guardar_usuarios(usuarios)
            print(f"'{nueva_cancion}' ha sido agregada a '{nombre_playlist}'!")
            ENTERContinuar()
        
        elif opcion == "3":
            if not playlist["canciones"]:
                print("No hay canciones para eliminar.")
                ENTERContinuar()
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
            ENTERContinuar()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
            ENTERContinuar()



