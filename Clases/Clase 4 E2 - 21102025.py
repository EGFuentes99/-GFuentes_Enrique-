# Haz un programa que pida tres números enteros y muestre si se cumple la expresión: El primer número es mayor que el segundo y el segundo es menor que el tercero. Esto sun utilizar condiciones, solo operadores lógicos.

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))
num3 = int(input("Ingresa el tercer número entero: "))

resultado = (num1 > num2) and (num2 < num3)

print(f"¿Se cumple la proposición? {resultado}")