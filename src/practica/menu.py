import os
os.system("cls" if os.name=="nt" else "clear")
nombre = "Alejandro Jacinto Uñate"
print(nombre)
print("-------------------------------------")
res = input("Desea Modificar el nombre o apellido: 's/n:' ")
print(" ")  
if res.lower()=="s":
    nombus = input("Ingrese aquí el nombre o apellido a cambiar: ").capitalize()
    buscar = nombre.find(nombus)
    if (buscar >= 0):
        nombre = nombre.replace(nombus, input("Ingrese la modificación: ").capitalize())
        print("Nombre Modificado: ".capitalize()+nombre)
        print(" ")
    else:
        print("No se encontro la palabra buscada, fin de ejecución".upper())
else:
    print("Gracias por participar, hasta pronto".upper())
print("-------------------------------------")
lista = list()
lista = nombre.replace(" ",",").split(",")
print(lista)
nom1, nom2, apel = lista
print(" ---------------------------------------------- ")
if res.lower()!= "s":
    print("no se modificó".upper())
else:
    print("si se modificó".upper())
print(f"primer nombre: {nom1} - segundo nombre: {nom2} - apellido: {apel}")
print(" ")