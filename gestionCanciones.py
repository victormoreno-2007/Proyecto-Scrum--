import json

ARCHIVO = 'usuarios.json'

def cargarDatos():
    try:
        with open(ARCHIVO, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Archivo 'ARCHIVO' no encontrado.")
        return {}

def guardarDatos(datos):
    with open(ARCHIVO, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def mostrarCanciones(playlist):
    canciones = playlist.get('canciones', [])
    if canciones:
        print("\nCanciones en la playlist:")
        for i, cancion in enumerate(canciones, 1):
            if isinstance(cancion, dict):
                print(f"{i}. {cancion.get('nombre', 'Sin título')} ({cancion.get('likes', 0)} likes)")
            else:
                print(f"{i}. {cancion}")
    else:
        print("No hay canciones en esta playlist.")

def darLikePorCancion(playlist):
    canciones = playlist.get('canciones', [])

    if not canciones:
        print("Esta playlist no tiene canciones.")
        return

    print("\nCanciones disponibles para dar like:")
    for i, cancion in enumerate(canciones, 1):
        if isinstance(cancion, dict):
            nombre = cancion.get("nombre", "Sin título")
            likes = cancion.get("likes", 0)
        else:
            nombre = cancion
            likes = 0
        print(f"{i}. {nombre} ({likes} likes)")

    try:
        opcion = int(input("Selecciona el número de la canción a la que quieres dar like: "))
        if 1 <= opcion <= len(canciones):
            cancionSeleccionada = canciones[opcion - 1]
            if isinstance(cancionSeleccionada, str):
                cancionSeleccionada = {"nombre": cancionSeleccionada, "likes": 1}
                canciones[opcion - 1] = cancionSeleccionada
            else:
                cancionSeleccionada["likes"] = cancionSeleccionada.get("likes", 0) + 1

            print(f"Has dado like a '{cancionSeleccionada['nombre']}'")
        else:
            print("Opción fuera de rango.")
    except ValueError:
        print("Entrada no válida. Por favor ingresa un número.")

def comentarPlaylist(playlist):
    comentario = input("Escribe tu comentario: ")
    comentarios = playlist.get('comentarios', [])
    comentarios.append(comentario)
    playlist['comentarios'] = comentarios
    print("Comentario agregado.")

def menuPlaylist(nombrePlaylist):
    datos = cargarDatos()
    playlist = datos.get('playlists', {}).get(nombrePlaylist)

    if not playlist:
        print(f"No se encontró la playlist '{nombrePlaylist}'.")
        return

    while True:
        print(f"\n--- Submenú Playlist: {nombrePlaylist} ---")
        print("1. Mostrar canciones")
        print("2. Dar like a una canción")
        print("3. Comentar playlist")
        print("4. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            mostrarCanciones(playlist)
        elif opcion == '2':
            darLikePorCancion(playlist)
            guardarDatos(datos)
        elif opcion == '3':
            comentarPlaylist(playlist)
            guardarDatos(datos)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    nombrePlaylist = input("Ingresa el nombre de la playlist que deseas abrir: ")
    menuPlaylist(nombrePlaylist)