#Elabora un programa que solicite alusuario un numero entero positivo y, usando un ciclo, determine si el mumero ingresado es primo o no. mostrando el resultado en la pantalla.
numero=int(input("Ingrese un numero entero positivo: "))
es_primo=True
if numero<2:
    es_primo=False
else:
        for i in range(2, int(numero**0.5)+1):
            if numero % i == 0:
                es_primo=False

if es_primo:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")

