import os
os.system("cls" if os.name == "nt" else "clear")
#dic = {"nombre": input("ingrese nombre:"),
#       "apellido": input("ingrese apellido:")}
#print(f"sus datos son: {dic}")

#nu1 = input("primer:")
#nu2 = input("segundo:")
#try:
#    print(int(nu1)+int(nu2))
#except ValueError:
#    print(f"no se puede convertir en entero {nu1} o {nu2}")
nu1 = input("Valor 1: ")
try:
    nu1 = int(nu1)
except ValueError:
    print(f"No se puede convertir {nu1} en entero")
    nu1 = 0
nu2 = input("Valor 2: ")
try:
    nu2 = int(nu2)
except ValueError:
    print(f"No se puede convertir {nu2} en entero")
    nu2 = 0
print(f"El resultado es: {nu1 + nu2}")
