def imprimir(nombre, apellido):
    i=0
    nombre2=""
    while (i<=len(nombre)-1):
        caracter = nombre[i]
        if (caracter==" "):
            i += 1
            nombre2 += " " + nombre[i].upper()
        else:
            nombre2 += caracter
        i = i + 1

    print(f"Nombre: {nombre2} - Apellido: {apellido}")
    input("Presione enter para continuar...".upper())
    valor = nombre2 + " " + apellido + " todo bien".upper()
    return valor

def sumar(a, b):
    resultado = int(a)+int(b)
    valor = "el resultado de la suma es: ".upper()
    valor = valor + str(resultado)
    return (valor)