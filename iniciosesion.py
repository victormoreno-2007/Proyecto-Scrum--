import json
import getpass

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

def registrar_usuario():
    usuarios = cargar_usuarios()
    
    print("\n--- Registro de nuevo usuario ---")
    usuario = input("Nombre de usuario: ")
    
    if usuario in usuarios:
        print("Este nombre de usuario ya existe.")
        return
    
    contraseña = getpass.getpass("Contraseña: ")
    confirmacion = getpass.getpass("Confirmar contraseña: ")
    
    if contraseña != confirmacion:
        print("Las contraseñas no coinciden.")
        return
    
    usuarios[usuario] = {
        "contraseña": contraseña,
        "playlist": []
    }
    guardar_usuarios(usuarios)
    print("Usuario registrado con éxito!")

def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    print("\n--- Inicio de Sesión ---")
    usuario = input("Nombre de usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"¡Bienvenido, {usuario}!")
        return usuario  # Devolvemos el nombre de usuario para usarlo después
    else:
        print("Usuario o contraseña incorrectos.")
        return None
    
PlaylistMenu = """
        Crear Playlist

    1. Ver mi playlist
    2. Agregar canción
    3. Eliminar canción
    4. Volver al menú principal
"""

def menu_playlist(usuario_actual):
    usuarios = cargar_usuarios()
    
    while True:
        print(PlaylistMenu)
        
        opcion = input("Seleccione una opción:\n -> ")
        
        if opcion == "1":
            print("\n--- Mis Canciones ---")
            if not usuarios[usuario_actual]["playlist"]:
                print("Tu playlist está vacía.")
            else:
                for i, cancion in enumerate(usuarios[usuario_actual]["playlist"], 1):
                    print(f"{i}. {cancion}")
            ENTERContinuar()

        elif opcion == "2":
            nueva_cancion = input("\nNombre de la canción a agregar: ")
            usuarios[usuario_actual]["playlist"].append(nueva_cancion)
            guardar_usuarios(usuarios)
            print(f"'{nueva_cancion}' ha sido agregada a tu playlist!")
            ENTERContinuar()
        
        elif opcion == "3":
            if not usuarios[usuario_actual]["playlist"]:
                print("No hay canciones para eliminar.")
                continue
                
            print("\n--- Seleccione canción a eliminar ---")
            for i, cancion in enumerate(usuarios[usuario_actual]["playlist"], 1):
                print(f"{i}. {cancion}")
            
            try:
                num = int(input("Número de canción a eliminar: "))
                if 1 <= num <= len(usuarios[usuario_actual]["playlist"]):
                    cancion_eliminada = usuarios[usuario_actual]["playlist"].pop(num-1)
                    guardar_usuarios(usuarios)
                    print(f"'{cancion_eliminada}' ha sido eliminada de tu playlist.")
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
                menu_playlist(usuario_actual)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()