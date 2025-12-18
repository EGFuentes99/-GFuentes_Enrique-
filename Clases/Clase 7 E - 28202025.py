# Ejercicio 3: Haz un programa en python que pida un número entero y muestre cuántos números pares hay desde 1 hasta ese número (incluyendolo su es par)

conteo_pares = 0
# Solicitar al usuario un número entero
numero_entero=int(input("Ingrese un numero entero: "))

for i in range(1, numero_entero + 1):
    if i % 2 == 0:
        conteo_pares += 1
    print(i)

print(f"Hay {conteo_pares} numeros pares desde 1 hasta {numero_entero}.")

# Ejercicio 4: Hz un programa en Python que pida un número y calcule el factorial de ese número usando un ciclo for.

numero = int(input("Ingrese un numero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es {factorial}.")

# Bucle While
# While condicion:
#   bloque de código

# Ejercicio 1: Haz un programa que pida al usuario ingresar una contraseña hasta que ingrese la correcta, y que tenga un máximo de 5 intentos.

# Definir la contraseña correcta
contraseña_correcta = "Credinalga"
intentos = 0
max_intentos = 5
contraseña = input("Ingrese la contraseña: ")

while (intentos < max_intentos) and (contraseña != contraseña_correcta):
    print("Contraseña incorrecta. Intente de nuevo.")
    intentos += 1
    contraseña = input("Ingrese la contraseña: ")

print("Contraseña correcta. Acceso concedido.")

# Ejercicio 2: Haz un programa que pida al usuario ingresar números pósitivos y que se detenga hasta que ingrese un número negativo

numero = float(input("Ingrese un numero positivo (o un numero negativo para salir): "))

while numero >= 0:
    numero = float(input("Ingrese un numero positivo (o un numero negativo para salir): "))

print("Numero negativo ingresado. Programa terminado.")

# Ejercicio 3: Haz un programa que sume todos los números que ingrese el usuario hasta que ingrese un 0.
suma_total = 0
numero = float(input("Ingrese un numero para sumar (0 para salir): "))

while numero != 0:
    suma_total += numero
    numero = float(input("Ingrese un numero para sumar (0 para salir): "))

print(f"La suma total de los números ingresados es: {suma}.")

