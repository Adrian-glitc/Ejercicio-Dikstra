import os
import sys

def main():
    while True:
        print("Selecciona un juego:")
        print("1. Juego de la Reina")
        print("2. Juego del Caballo")
        print("3. Salir")
        
        opcion = input("Ingresa el número de tu elección: ")
        
        if opcion == "1":
            ejecutar_juego("reina")
        elif opcion == "2":
            ejecutar_juego("caballo")
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def ejecutar_juego(juego):
    ruta_juego = os.path.join(os.path.dirname(__file__), juego, "main.py")
    if os.path.exists(ruta_juego):
        print(f"Iniciando el juego de {juego}...")
        os.system(f'python "{ruta_juego}"')
    else:
        print(f"No se encontró el archivo principal para el juego de {juego}.")

if __name__ == "__main__":
    main()