import os
os.system("cls" if os.name=="nt" else "clear")
#casos=int(input("ingrese una opción: ".upper()))
a = 2
b = 2
def switch_case(casos):
    if casos == 1:
        b = 1
        a = 2
        return "Caso 1"
    elif casos == 2:
        return "Caso 2"
    elif casos == 3:
        return "Caso 3"
    else:
        return "Caso por defecto"

# Ejemplos de uso
print(switch_case(casos=int(input("ingrese una opción: ".upper()))))  # Output: "Caso 1"
if not((b==1) | (a ==2)):
    print("todo bien".upper())
    pass

#print(switch_case(4))  # Output: "Caso por defecto"
