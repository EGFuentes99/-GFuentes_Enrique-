#Pide un numero entero y determina si es divisible entre 4, 6 o ambos
def verificar_divisivilidad():
    numero = int(input("Ingrese un número entero: "))
    if numero % 4 == 0 and numero % 6 == 0:
        print(f"El número {numero} es divisible entre 4 y 6.")
    elif numero % 4 == 0:
        print(f"El número {numero} es divisible entre 4.")
    elif numero % 6 == 0:
        print(f"El número {numero} es divisible entre 6.")
    else:
        print(f"El número {numero} no es divisible entre 4 ni 6.")
verificar_divisivilidad()  