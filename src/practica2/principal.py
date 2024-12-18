import funciones_externas
import os
os.system("cls" if os.name=="nt" else "clear")
devo=funciones_externas.imprimir(input("Ingrese Nombre: ").capitalize(), input("Ingrese Apellido: ").capitalize())
print(devo)
input()
os.system("cls" if os.name=="nt" else "clear")