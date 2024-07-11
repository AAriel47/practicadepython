import os
os.system("cls" if os.name=="nt" else "clear")
datos = list()
print("consulta de alumnos".upper().center(95))
print("-".rjust(100,"-"))
if (os.path.exists("misdatos.txt")):
    archi = open("misdatos.txt","r",encoding="utf-8")
    lineas = archi.readlines()
    i = 0
    for lineas2 in lineas:
        lineas3 = lineas2.split(" ")
        if (len(lineas3)> 4):
            print(f"Primer nombre: {lineas3[0]}  -  Segundo nombre: {lineas3[1]} {lineas3[2]} - Apellido: {lineas3[3]} -  Código: {lineas3[4]}")
        else:
            print(f"Primer nombre: {lineas3[0]}  -  Segundo nombre: {lineas3[1]} - Apellido: {lineas3[2]} - Código: {lineas3[3]}")
        lineas3.clear()
        i = i + 1
        if (i==4):
            input("presione cualquier tecla".upper())
            i = 0
            os.system("cls" if os.name=="nt" else "clear")
else:
    print("el archivo misdatos.txt no existe".upper().center(95))
print("-".rjust(100,"-"))
print("final de la consulta".upper().center(95))
print("-".rjust(100,"-"))