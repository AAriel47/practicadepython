import subprocess
import os
os.system("cls" if os.name=="nt" else "clear")
def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Alta de alumnos")
    print("2. Consulta de alumnos")
    print("3. Borrado de alumnos")
    print("4. Modificacion de alumnos")
    print("5. Salir")

def ejecutar_archivo(opcion):
    if opcion == '1':
        subprocess.run(['python', 'usodefor.py'])
    elif opcion == '2':
        subprocess.run(['python', 'consulta.py'])
    elif opcion == "3":
        subprocess.run(["python","borrar.py"])
    elif opcion == "4":
        subprocess.run(["python","modificar.py"])
    elif opcion == '5':
        print("Saliendo...")
    else:
        print("Opción no válida, por favor intenta de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingresa tu opción: ")
        if opcion == '5':
            ejecutar_archivo(opcion)
            os.system("cls" if os.name=="nt" else "clear")
            break
        else:
            ejecutar_archivo(opcion)

if __name__ == "__main__":
    main()
