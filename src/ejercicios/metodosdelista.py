import os

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')
lista = list()
print(type(lista))
lista.append("alejandro")
lista.insert(0,"ariel")
lista.extend(["uñate","santa ana"])
lista.append("masculino")
print(lista)
print(len(lista))
lista.pop(-1)
lista.append("profesor")
print(lista)
lista.remove("profesor")
print(lista)
lista1 = [1,2,3,4,5]
print(lista1)
#lista1.sort(reverse=True)
lista1.reverse()
print(lista1)
lista1.clear()
print(lista1)

