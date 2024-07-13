import os
os.system("cls" if os.name=="nt" else "clear")
archi = "misdatos.txt"
alumno = list()
alumno1 = list()
datos2 = list()

if (os.path.exists(archi)):
    archi1 = open(archi,"r",encoding="utf-8")
    alumno = archi1.readlines()
    seguir = True
else:
    print("archivo misdatos.txt, no existe".upper())
    seguir = False

while (seguir==True):
    print("modificación de datos de misdatos.txt".upper().center(100))
    print("-".rjust(100,"-"))
    print("seleccione un código de alumno".center(100))
    print("-".rjust(35,"-").center(100))
    i = 1
    for alumnos in alumno:
        alumno1 = alumnos.split(" ")
        if(len(alumno1)>4):
            print(f"Primer nombre: {alumno1[0]} - Segundo nombre: {alumno1[1]} {alumno1[2]}- Apellido: {alumno1[3]} - Codigo: {alumno1[4]}")
        else:
            print(f"Primer nombre: {alumno1[0]} - Segundo nombre: {alumno1[1]} - Apellido: {alumno1[2]} - Codigo: {alumno1[3]}")
        i+=1
        if(i==5):
            input("Presione enter para continuar...".capitalize())
            os.system("cls" if os.name=="nt" else "clear")
    control = True
    while (control==True):
        codi=input("código del alumno:".upper())
        print("-\n".rjust(35,"-"))
        if (codi.isnumeric()):
            control=False
        else:
            print("Por favor ingrese un número...\n".upper()) 
            print("-\n".rjust(35,"-"))
            print("Presione enter para continuar...\n".upper())
            input()
            os.system("cls" if os.name=="nt" else "clear")

    cont = 0
    paso1 = False
    for codigo in alumno:
        conf=codigo.find(codi)
        if(conf==-1):
            cont += 1
        else:
            datos1 = codigo.split(" ")
            paso1 = True
        if(len(alumno)==cont):
            print(f"existen {cont} codigos de alumnos...\n".capitalize())
            paso1 = False
            print("El alumno buscado no existe\n".upper())
            print("-\n".rjust(35,"-"))

    while (paso1):
        print(f"Primer nombre: {datos1[0]}\n")
        if (len(datos1)>5):
            print(f"Segundo nombre: {datos1[1]} {datos1[2]}\n")
            print(f"Apellido: {datos1[3]}\n")
        else:
            print(f"Segundo nombre: {datos1[1]}\n")
            print(f"Apellido: {datos1[2]}\n")
        print("-\n".rjust(35,"-"))
        datos2=[input("Primer nombre: \n").capitalize(),
            input("Segundo nombre: \n").capitalize(),
            input("Apellido: \n").capitalize(),
            str(codi)
            ]
        print(" ")
        print("-\n".rjust(35,"-"))

        nuevo = f"{datos2[0]} {datos2[1]} {datos2[2]} {datos2[3]}\n"
        alumno.pop(int(codi)-1)
        alumno.insert((int(codi)-1),nuevo)
        grabar = input("desea grabar el registro s/n: \n".upper())
        if ((grabar.lower()=="s")| (grabar.lower()=="si")):
            if (os.path.exists(archi)):
                archi1 = open(archi,"w",encoding="utf-8")
                archi1.writelines(alumno)
                archi1.close()
                print("Registro Guardado, pulse enter para continuar...\n".upper())
                input()
            else:
                print("no se pudo guardar, el archivo misdatos.txt fue eliminado, pulse enter para continuar...\n".upper())
                input()
        elif((grabar.lower()=="n")| (grabar.lower()=="no")):
            print("El registro no se guardó, pulse enter para continuar...\n".upper())
            input()
        else:
            print("opcion no válida\n".upper())
            input()
        paso1=False

    seguir1=input("Desea continuar s/n: ".upper())
    if((seguir1.lower()=="s")|(seguir1.lower()=="si")):
        seguir=True
    else:
        os.system("cls" if os.name=="nt" else "clear")
        seguir=False