import json

# Este el la direccion del archivo json donde estan los diccionarios
archivoJson = 'informacionCantantes.json'

#Funcion para leer el json 
def leerJson():
    try:
        with open(archivoJson,'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo no se encuentra")
        return
    except json.JSONDecodeError:
        print("Error al leer json")
        return

