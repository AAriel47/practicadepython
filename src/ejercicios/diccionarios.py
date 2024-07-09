import os

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')
diccionario={"nombre": "alejandro",
             "apellido": "uñate",
             "dni": 25025114}
print(diccionario.keys())
print(diccionario.get("apellido"))
#print(diccionario.pop("nombre"))
#print(diccionario)
valor=diccionario.items()
print(type(valor))
print(valor)
#diccionario.clear()
print(diccionario.values())
print(dir(diccionario))