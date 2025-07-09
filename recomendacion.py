import json
import os

def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enterParaContinuar(Continuar="\nPresione ENTER para continuar\n -> "):
    input(Continuar)
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
        
        while True: 
            try:
                buscadorGenero = input("Seleciona el genero por nombre: \n").strip()
                if buscadorGenero not in generos:
                    raise ValueError("Genero no existe,ingresa de nuevo el genero")
                    enterParaContinuar()
                    limpiarConsola()
                    print("Los géneros disponibles son:\n")
                    for i, genero in enumerate(generos, 1):
                        print(f"{i}. {genero}")
                    continue
                break     
            except (ValueError, Exception) as a:
                print(f"Upss, salio un error inesperado: {a}")
                enterParaContinuar()
                limpiarConsola()
                print("Los géneros disponibles son:\n")
                for i, genero in enumerate(generos, 1):
                    print(f"{i}. {genero}")
                continue
                
        cantantes = generos[buscadorGenero]
        print(f"\n Cantates recomendados en {buscadorGenero}")
        for i, singer in enumerate(cantantes, 1):
            print(f"{i}. {singer['nombre']}")

        while True:
            verCanciones = input("\n¿Quieres ver las mejores canciones de alguno? (si/no):\n ").strip().lower()
            if verCanciones == "si":
                while True:
                    nombre = input("Escribe el nombre del cantante exactamente como aparece: ").strip()
                    cantanteEncontrado = next((a for a in cantantes if a["nombre"].lower() == nombre.lower()), None)
                    if cantanteEncontrado:
                        print(f"\n Mejores canciones de {cantanteEncontrado['nombre']}:")
                        for cancion in cantanteEncontrado["canciones"]:
                            print(f"- {cancion}")
                            
                        break
                    else:
                        print("Cantante no encontrado. Asegurate de escribirlo bien")
                        
                        break
            elif verCanciones == "no":
                print(" Entendido. No se mostraran canciones.")
                enterParaContinuar()
                limpiarConsola()
                return
                
            else:
                print("Respuesta no reconocida. Por favor escribe 'si' o 'no'.")
                
            
            
    #Funcion mostrar cantantes top globales mediante una lista        
def mostrarTopGlobal(datos):
        print("\n Top 10 cantantes globales: \n")
        for  cantante in datos["topGlobal"]:
            print(f" {cantante}")

    #Funcion mostrar cantantes top colombia mediante una lista  
def mostrarTopColombia(datos):
        print("\n Top 10 cantantes colombia: \n")
        for  cantante in datos["topColombia"]:
            print(f" {cantante}")

    #Funcion de menu interactivo para recomendaciones

def menuRecomendaciones():
        archivo = leerJson()
        while True:
            print('''
            Menu de recomenaciones de cantantes
            
            1.Ver recomendaciones de cantantes por genero
            2.Ver lista de cantantes Top globales
            3.Ver lista de cantantes Top colombia
            4.Salir
            ''')
            opcion= input(f"ingrese la opcion que desea: \n")

            if opcion == "1":
                mostrarXGeneros(archivo)
                enterParaContinuar()
                limpiarConsola()
            elif opcion == "2":
                mostrarTopGlobal(archivo)
                enterParaContinuar()
                limpiarConsola()
            elif opcion == "3":
                mostrarTopColombia(archivo)
                enterParaContinuar()
                limpiarConsola()
            elif opcion == "4":
                print("Gracias por usar este menu")
                enterParaContinuar()
                limpiarConsola()
                break
            else:
                print("Ingrese una opcion valida ")
        
