import os
os.system("cls" if os.name =="nt" else "clear")
letras = "arielalejeangmail"
num = "112345"
completo = "Alejandro Ariel Uñate Masculino 48 Argentio"
#funciones
print(dir(letras))
print(type(letras))
print(len(letras))
#metodos
print(num.isnumeric())
print(letras.isalpha())
print(letras.count("a"))
print(letras.find("m"))
print(letras.index("a"))
print(letras.startswith("ariel"))
print(letras.endswith("ail"))
#print(letras.replace("ean","andro."))
nuevo = completo.replace(" ",",")
print(nuevo.split(","))
print(letras.upper())
print(letras.lower())
print(letras.capitalize())


