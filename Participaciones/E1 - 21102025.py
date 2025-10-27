#Haz un programa que solicite al usuario la base y la altura de un rectángulo y calcule su área y perímetro.

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

