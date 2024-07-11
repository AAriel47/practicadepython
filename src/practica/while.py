import os
os.system("cls" if os.name=="nt" else "clear")

archivo = "datos.txt"
continuar = "s"
alumnos = list()
alumnos2 = list()
while continuar == "s":
    print("------------------------( Alumnos de 4 A - Comisión 2024 )------------------------")
    dic = {"Nombre1": input("Ingrese el Primer Nombre:     ".capitalize()).capitalize(),
        "Nombre2": input("Ingrese el segundo Nombre:    ".capitalize()).capitalize(),
        "Apellido": input("Ingrese el apellido:          ".capitalize()).capitalize()
        }
    print("----------------------------------------------------------------------------------")
    res = input("desea grabar s/n: ".capitalize())
    if (res.lower()=="s"):
        nom1, nom2, apel = dic["Nombre1"],dic["Nombre2"],dic["Apellido"]
        alumnos.append(nom1)
        alumnos.append(nom2)
        alumnos.append(apel)

        alumnos2.append(nom1)
        alumnos2.append(" ")
        alumnos2.append(nom2)
        alumnos2.append(" ")
        alumnos2.append(apel)
        alumnos2.append("\n")

        if os.path.exists(archivo):
            archivos = open("datos.txt","a", encoding="utf-8")
            archivos.writelines(alumnos2)
            archivos.close()
        else:
            with open("datos.txt","w", encoding="utf-8") as archivos:
                archivos.writelines(alumnos2)
                archivos.close()
        alumnos2.clear()
        a = 0
        b = 1
        c = 2
        print("---------------------------- <<< Informe final >>> ----------------------------".upper())
        while (a<=len(alumnos)-1):
            print(f"Primer Nombre: {alumnos[a]} - Segundo Nombre: {alumnos[b]} - Apellido: {alumnos[c]}")
            print("-----------------------------------------------------------------------------------")
            a += 3
            b += 3
            c += 3
            print("")
            if(a==len(alumnos)-1):
                exit
        print("El registro se grabó")
    else:
        print(" ")
        print("El registro no se guardo")
    print("--------------------------------")
    continuar = input("Desea continuar s/n: ").lower()
    if (continuar=="s"):
        os.system("cls" if os.name=="nt" else "clear")
    else:
        print("Hasta pronto, gracias por usar mis servicios".upper())
    print(" ")

