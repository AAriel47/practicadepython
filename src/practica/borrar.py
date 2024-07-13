def main():
    import os
    os.system("cls" if os.name=="nt" else "clear")
    archi = "misdatos.txt"
    seguir = False
    if (os.path.exists(archi)):
        datos=open(archi,"r",encoding="utf-8")
        lineas = datos.readlines()
        datos.close()
        seguir=True
    else:
        print("el archivo \"misdatos.txt\" fue borrardo, pulse enter para continuar...".upper())
        input()
        os.system("cls" if os.name=="nt" else "clear")

    while (seguir==True):
        for lineas1 in lineas:
            print(lineas1)
        
        cod=input("ingrese el codigo: ")
        cod2 = int(cod)
        if ((cod2<=len(lineas))&(cod2>0)):
            i = 0
            lista=list()
            entrar = 0
            for lineas2 in lineas:
                valor = lineas2.find(cod)

                if (valor!=-1):
                    e = i
                    entrar = 1
                elif (entrar==1):
                    o = i + 1
                    lineas3 = lineas2.replace(str(o), str(i))
                    lista.append(lineas3)
                i+= 1
                
            res=input("borrar s/n: ".lower())
            if ((res.lower()=="s") | (res.lower()=="si")):
                while (e<=(len(lineas)-1)):
                    lineas.pop(e)
                for agregar in lista:
                    lineas.append(agregar)
                if(os.path.exists(archi)):
                    archi1 = open(archi,"w",encoding="utf-8")
                    archi1.writelines(lineas)
                    archi1.close
                else:
                    with open(archi,"w",encoding="utf-8") as archi1:
                        archi1.writelines(lineas)
                        archi1.close()
                print(lineas)
                print("El registro se borro")
                #exit()
            else:
                print("el registro no se borro")
                continue
        else:
            print("codigo invalido, no existe")
            input()
        seguir1 = input("Desea continuar s/n: ".upper()).lower()
        if ((seguir1=="s") | (seguir1=="si")):
            seguir=True
        else:
            seguir=False
if __name__ == "__main__":
    main()
