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
#Funcion para recomendacion de cantantes segun el genero y tambien sus mejores canciones si asi lo desea el usuario
def mostrarXGeneros(datos):
    generos= datos['generos']
    print("Los generos disponibles disponibles:\n")
    for i, genero in enumerate(generos,1):
        print(f"{i}. {genero}")
    try: 
        buscadorGenero = input("Seleciona el genero por nombre: \n").strip()
        if buscadorGenero not in generos:
            raise ValueError("Genero no existe,ingresa de nuevo el genero")
        
        cantantes = generos[buscadorGenero]
        print(f"\n Cantates recomendados en {buscadorGenero}")
        for i, singer in enumerate(cantantes, 1):
            print(f"{i}. {singer['nombre']}")
        verCanciones = input(f"\n Quieres ver las mejores canciones de algun cantante? (si/no)").strip().lower()
        if verCanciones == "si":
            numeroCantante = input("Selecciona el numero del cantante: ").strip()
            if not numeroCantante.isdigit():
                raise ValueError("Debes ingresa un numero valido") 
            numeroCantante = int(numeroCantante)-1
            if not (0<= numeroCantante < len(cantantes)):
                raise IndexError("Numero invalido")

            canciones = cantantes[numeroCantante].get("canciones", [])
            print(f"\n Mejores caciones de {cantantes[verCanciones]['nombre']}:") 
            for i,cancion in canciones:
                print(f"{i}. {cancion}")

        elif verCanciones == "no":
            print("Esta bien no se mostraran las canciones") 
        else:
            print("Pusiste opcion invalida es si o no") 
    except ValueError as a:
        print(a)
    except IndexError as e:
        print(e)
    except Exception as ae:
        print(f"Upss, salio un error inesperado: {ae}")
        
