def main():
    import os
    os.system("cls" if os.name=="nt" else "clear")

    centro = 100
    archi = "misdatos.txt"
    seguir = "s"
    datos = list()
    if (os.path.exists(archi)):
        lineas1 = list()
        archi2 = open(archi,"r",encoding="utf-8")
        lineas = archi2.readlines()
        #lineas1 = lineas.
        #print (type(lineas))
        codigo1 = lineas[len(lineas)-1]
        lineas1 = codigo1.split(" ")
        codigo = int(lineas1[len(lineas1)-1])+1
        print(codigo)
    else:
        codigo = len(datos) + 1

    relleno = ("-".rjust(100,"-"))
    while (seguir != "n"):
        print("ingreso de datos".upper().center(centro))
        print(relleno)
        datos = [input("Ingrese el primer Nombre:  ".upper()).capitalize(),
                " ",
                input("ingrese el segundo Nombre: ".upper()).capitalize(),
                " ",
                input("Ingrese el Apellido:       ".upper()).capitalize(),
                " ",
                str(codigo),
                "\n"
                ]
        print(f"Código único del Alumno: {codigo}    ".upper())
        print("-".rjust(100,"-"))
        resp = input("Desea guardar los datos s/n: ")
        #nom1, nom2, apel, codi = datos
        #print("-".rjust(100,"-"))
        if (resp.lower()=="s"):
            if (os.path.exists(archi)):
                archi2 = open(archi,"a",encoding="utf-8")
                archi2.writelines(datos)
                archi2.close()
            else:
                with open(archi,"w", encoding="utf-8") as archi2:
                    archi2.writelines(datos)
                    archi2.close()
            print("-".rjust(100,"-"))
            print("Datos almacenados en la base de datos".upper())
        else:
            print("-".rjust(100,"-"))
            print("los datos no se almacenaron en la base de datos".upper())
        print("-".rjust(100,"-"))
        seguir = input("desea seguir s/n: ".capitalize())
        if (seguir.lower()=="n"):
            os.system("cls" if os.name=="nt" else "clear")
            exit
        else:
            codigo += 1
            os.system("cls" if os.name=="nt" else "clear")
            datos.clear()
            continue
if __name__ == "__main__":
    main()
