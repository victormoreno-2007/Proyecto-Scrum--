import json 

with open('usuarios.json', 'r') as file:
    informacion = json.load(file)

for clave,nombre in informacion.item():
    print(f'usuario: {clave}')
    playlist = nombre.get('playlist', {})
    if playlist:
        print('playlist:')
        for nom_playlist in playlist:
            print(f'{nom_playlist}')

    else:
        print('aun no hay playlist registradas')



def verMisPlaylist():
    
    try:
        with open('usuarios.josn', 'r' )as file:
            playlist = json.load(file)
        print('contactos actuales: ')
        for item in playlist:
            print(item)
    except FileNotFoundError  :
        print('aun no hay contactos guardados')
      