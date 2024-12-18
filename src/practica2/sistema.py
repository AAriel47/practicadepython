import os
import subprocess
os.system("cls" if os.name=="nt" else "clear")
def mostrar():
    print("Seleccione una opción".upper())
    print("1. Alta".upper())
    print("2. consulta".upper())
    print("3. Salir".upper())

def ejecutar(opcion):
    if opcion=="1":
        subprocess.run(["python","alta.py"])
        os.system("cls" if os.name=="nt" else "clear")
    if opcion=="2":
        subprocess.run(["python","consulta.py"])
        os.system("cls" if os.name=="nt" else "clear")
    if opcion=="3":
        print("hasta pronto...".capitalize())

def main():
    while True:
        mostrar()
        opcion=input("Seleccione una opción:  ".upper())
        if opcion=="3":
            ejecutar(opcion)
            input()
            os.system("cls" if os.name=="nt" else "clear")
            break
        else:
            ejecutar(opcion)

if __name__=="__main__":
    main()
