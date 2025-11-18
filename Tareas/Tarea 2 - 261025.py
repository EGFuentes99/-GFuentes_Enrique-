# Ejercicio 1: Haz un programa en Python que pida tres calificaciones y calcule su promedio con dos decimales

calificacion1 = float(input("Ingresa la primera calificación: "))
calificacion2 = float(input("Ingresa la segunda calificación: "))
calificacion3 = float(input("Ingresa la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3
print(f"El promedio de las calificaciones es: {promedio:.2f}")

# Ejercicio 2: Haz un programa en Python que calcule el área de un círculo a partir de su radio

import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2

print(f"El área del círculo con radio {radio} es: {area:.2f}")

# Ejercicio 3: Haz un programa en Python que calcule el perímetro de una circunferencia con base en su radio

import math
radio = float(input("Ingresa el radio de la circunferencia: "))
perimetro = 2 * math.pi * radio

print(f"El perímetro de la circunferencia con radio {radio} es: {perimetro:.2f}")

# Ejercicio 4: Haz un programa en Python que convierta una cantidad de minutos a horas

minutos = int(input("Ingresa la cantidad de minutos: "))
horas = minutos / 60

print(f"{minutos} minutos son equivalentes a {horas:.2f} horas.")

# Ejercicio 5: Haz un programa en Python que pida un precio y muestre el total con IVA del 16%

precio = float(input("Ingresa el precio del producto: "))
iva = precio * 0.16
total_con_iva = precio + iva

print(f"El total con IVA del 16% es: {total_con_iva:.2f}")

# Ejercicio 6: Haz un programa en Python que pida tres números y muestre si se cumple la expresión A < B < C (solo mostrando el resultado lógico).

numA = float(input("Ingresa el primer número (A): "))
numB = float(input("Ingresa el segundo número (B): "))
numC = float(input("Ingresa el tercer número (C): "))

resultado = (numA < numB) and (numB < numC)
print(f"¿Se cumple la expresión A < B < C? {resultado}")

# Ejercicio 7: Haz un programa en Python que pida un número y muestre si está entre 10 y 20 (solo mostrando True o False).

numero = float(input("Ingresa un número: "))
esta_entre_10_y_20 = (numero > 10) and (numero < 20)
print(f"¿El número está entre 10 y 20? {esta_entre_10_y_20}")

# Ejercicio 8: Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False).

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

son_iguales = (num1 == num2) and (num2 == num3)
print(f"¿Los tres números son iguales? {son_iguales}")

# Ejercicio 9: Haz un programa en Python que pida tres números y muestre si los tres son iguales (solo mostrando True o False).

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

son_diferentes = (num1 != num2) and (num1 != num3) and (num2 != num3)
print(f"¿Los tres números son diferentes? {son_diferentes}")

# Ejercicio 10: Haz un programa en Python que pida el radio y la altura de un cilindro y muestre su volumen.
import math

radio = float(input("Ingresa el radio del cilindro: "))
altura = float(input("Ingresa la altura del cilindro: "))
volumen = math.pi * radio**2 * altura

print(f"El volumen del cilindro es: {volumen:.2f}")

