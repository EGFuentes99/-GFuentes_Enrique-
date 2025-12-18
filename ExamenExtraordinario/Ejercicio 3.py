#Crea un programa que solicite al usuario una cantidad indeterminada de numeros enteros hasta que se ingrese el valor 0, almacenandolos en una lista y mostrando al final el mayor, el menor y la suma total de los numeros capturados.
numeros = []
while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero) 
if numeros:
    mayor = max(numeros)
    menor = min(numeros)
    suma = sum(numeros)
    print(f"El numero mayor es: {mayor}")
    print(f"El numero menor es: {menor}")
    print(f"La suma total de los numeros es: {suma}")

else:
    print("No se ingresaron numeros.")
    