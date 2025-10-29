# Ejercicio 1: Haz un programa en Python que pida un número, posteriormente muestra todos los números desde 1 hasta el número ingresado. Imprime en consola un conteo de números pares y de números impares.

conteo_pares = 0
conteo_impares = 0
# Solicitar al usuario un número
numero_entero=int(input("Ingrese un numero entero: "))
for i in range(1, numero_entero + 1):
    if i % 2 == 0:
        conteo_pares += 1
    else:
        conteo_impares += 1

print(f"Hay {conteo_pares} numeros pares y {conteo_impares} numeros impares desde 1 hasta {numero_entero}.")

# Ejercicio 2: Haz un programa que pida al ususario ungresar un nombre y una edad, verifica si la persona ingresada tiene la edad suficiente para votar (Tomando en cuenta que se puede votar a partir de los 18 años), si puede votar imprime un mensaje indicándo que se puede votar, en caso de que no se pueda, imprime un mensaje indicando que no se puede votar y los años que faltan para poder votar.

nombre = input("Ingrese su nombre prro: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"{nombre}, usted tiene {edad} años y puede votar.")
else:
    años_faltantes = 18 - edad
    print(f"{nombre}, usted tiene {edad} años y no puede votar. Le faltan {años_faltantes} años para poder votar.")

# Ejercicio 3: Haz un programa en Python que pida al usuario ingresar un número y muestre su tabla de multipicar del 1 al 20, pero solo para los múltiplos pares (Es decir, numero x 2, número x 4, número x 6, etc.).

número = int(input("Ingrese un número para ver su tabla de multiplicar (solo múltiplos pares): "))
print(f"Tabla de multiplicar del {número} (múltiplos pares):")
for i in range(2, 21, 2):
    resultado = número * i
    print(f"{número} x {i} = {resultado}")

# Ejercicio 4: Haz un programa que pida 5 números (Técnicamente podríamos almacenarlos en un arreglo, pero no hemos llegado ahí, así que NO LO HAGAS ASÍ, debes pedir los números y almacenarlos en variables diferentes), de los 5 números ingresados, muestra cuántos fueron mayores que 10.

num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))   
num3 = float(input("Ingrese número 3: "))
num4 = float(input("Ingrese número 4: "))
num5 = float(input("Ingrese número 5: "))

conteo_mayores_10 = 0
if num1 > 10:
    conteo_mayores_10 += 1
if num2 > 10:
    conteo_mayores_10 += 1
if num3 > 10:
    conteo_mayores_10 += 1
if num4 > 10:
    conteo_mayores_10 += 1
if num5 > 10:
    conteo_mayores_10 += 1

print (f"De los 5 números ingresados, {conteo_mayores_10} son mayores que 10.")

# Ejercicio 5: Haz un programa que sume todos los números pares del 1 al 100. Al final muestra el resltado de la suma.

suma_pares = 0
for i in range(1, 100 + 1):
    if i % 2 == 0:
        suma_pares += i
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}.")

# Ejercicio 6: Haz un programa que genere la tabla de multiplicar de un número ingresado. Al final, muestra cuántos resultados de las multiplicaciones fueron mayores que 50 y cuantos iguales a 50.
número = int(input("Ingrese un número para ver su tabla de multiplicar: "))

conteo_mayores_50 = 0
conteo_iguales_50 = 0
print(f"Tabla de multiplicar del {número}:")
for i in range(1, 10 + 1):
    resultado = número * i
    print(f"{número} x {i} = {resultado}")
    if resultado > 50:
        conteo_mayores_50 += 1
    if resultado == 50:
        conteo_iguales_50 += 1
    
print(f"En la tabla de multiplicar del {número}, hay {conteo_mayores_50} resultados mayores que 50 y {conteo_iguales_50} resultados iguales a 50.")
