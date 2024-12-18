import funciones_externas
import os
os.system("cls" if os.name=="nt" else "clear")
while True:
    try:
        print(funciones_externas.sumar(input("a: "), input("b: ")))
        break
    except ValueError:
        os.system("cls" if os.name=="nt" else "clear")
        input("error al ingresar los datos, presione enter...".upper())
        continue

