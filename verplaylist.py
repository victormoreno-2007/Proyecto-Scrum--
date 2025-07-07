import json 

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
            plailists = informacion[usuario].get('playlist', {})
            if plailists:
                print(f'playlists del usuario {usuario}')
                for nombre, contenido in plailists.items():
                    print(f'{nombre}: {contenido['descripcion']}')
            else:
                print('aun no tienes playlist')
        else:
            print('el usuario no existe')
            
    except FileNotFoundError:
        print('no se encontro el archivo usuarios.json')
      