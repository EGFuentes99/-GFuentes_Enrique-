#Pide un número entero y calcula cuántos números impares existen entre 1 y N
def contar_impares_hasta_n():
    n = int(input("Ingrese un número entero positivo N: "))
    if n < 1:
        print("Por favor, ingrese un número entero positivo mayor o igual a 1.")
        return
    contador_impares = 0
    for i in range (1, n + 1):
        if 1 % 2 != 0:
            contador_impares += 1
    print(f"Hay {contador_impares} números impares entre 1 y {n}.")
contar_impares_hasta_n() 