import json
import getpass
from verplaylist import verMisPlaylist

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

PlaylistMenu = """
        Gestión de Playlists

    1. Ver mis playlists
    2. Crear nueva playlist
    3. Seleccionar playlist
    4. Volver al menú principal
"""

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
    usuarios = cargar_usuarios()
    
    while True:
        print(PlaylistMenu)
        
        opcion = input("Seleccione una opción:\n -> ")
        
        if opcion == "1":
            verMisPlaylist(usuario_actual)

        elif opcion == "2":
            crearPlaylist(usuario_actual)
        
        elif opcion == "3":
            usuarios = cargar_usuarios()
            
            if not usuarios[usuario_actual]["playlists"]:
                print("No tienes playlists creadas. Crea una primero.")
                ENTERContinuar()
                continue
                
            print("\n--- Seleccionar playlist ---")
            for i, nombre in enumerate(usuarios[usuario_actual]["playlists"].keys(), 1):
                print(f"{i}. {nombre}")
            
            try:
                num = int(input("Número de la playlist a gestionar: "))
                lista_playlists = list(usuarios[usuario_actual]["playlists"].keys())
                if 1 <= num <= len(lista_playlists):
                    playlist_seleccionada = lista_playlists[num-1]
                    menu_gestion_playlist(usuario_actual, playlist_seleccionada)
                else:
                    print("Número inválido.")
                    ENTERContinuar()
            except ValueError:
                print("Por favor ingrese un número válido.")
                ENTERContinuar()
        
        elif opcion == "4":
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

MenuPrincipal = """
        Menú Principal

    1. Iniciar sesión
    2. Registrar nuevo usuario
    3. Salir
"""

def menu_principal():
    while True:
        print(MenuPrincipal)
        
        opcion = input("Seleccione una opción:\n -> ")
        
        if opcion == "1":
            usuario_actual = iniciar_sesion()
            if usuario_actual:
                menu_playlists(usuario_actual)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()