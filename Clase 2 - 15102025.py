Programa saludo o bienvenida
nomrbre = input("Ingrese su nombre completo:")
edad = int(input("ingrese su edad: ")) #int() realiza un parseo de datos para convertir el dato ingresado en entero, ya que por defecto input() devuelve un string
estatura = float(input("Ingrese su carrera: "))
carrera = input("Ingrese su carrera: ") 

# print(f"Hola {nombre}, tienes {edad} años, mides {estatura} metros y estudias {carrera}. Bienvenido a la clase de Introducción a la Programación")

#Calculadora básica
num1 = 12
num2 = float(input("Ingrese un número (Puedeser decimal): "))

#Suma
suma = num1 + num2
print(f"La suma de {num1} + {num2} es: {suma}")

#Resta
resta = num1 - num2
print(f"La resta de {num1} - {num2} es: {resta}")

#Multiplicación
multiplicación = num1 * num2
print(f"La multiplicación de {num1} * {num2} es: {multiplicación}")

#División (Flotante), es decir, puede incluir decimales
divisiónFlotante = num1 / num2
print(f"La división de {num1} / {num2} es: {divisiónFlotante}")

#División entera, solo me va a devolver la parte entera del resultado
divisiónEntera = num1 // num2
print(f"La división de {num1} // {num2} es: {divisiónEntera}")

#Módulo, me devuelve el residuo de la división
módulo = num1 % num2
print(f"El módulo de {num1} % {num2} es: {módulo}")

#Potencia
potencia = num1 ** num2
print(f"La potencia de {num1} ** {num2} es: {potencia}")





#Operaciones con la librería Math
num1 = 100
num2 = 3

#Raíz cuadrada
raísCuadrada = math.sqrt(num1)
print(f"La raíz cuadrada de {num1} es: {raízCuadrada}")

#Potencia
potencia = math.sqrt(num1)
print(f"La potencia de 3 elevado a 3 es: {potencia}")

#PI con MATH
print(f"El valor de PI es: {math.pi}")

#Número e
print(f"El valor de e es: {math.e}")

#Redondeo hacia arriba
redondeoHaciaArriba = math.cei(3.4)
print(f"El redondeo hacia arriba de 3.4 es: {redondeoHaciaArriba}")

#Redondeo hacia abajo
redondeoHaciaAbajo = math.cei(3.7)
print(f"El redondeo hacia abajo de 3.7 es: {redondeoHaciaAbajo}")

#Operadores de comparación
num1 = 7
num2 = 5

#Igualdad (==)
print(f"¿El número {num1} es diferente a {num2}? {num1 == num2}")

#Desigualdad (!=)
print(f"¿El número {num1} es mayor que {num2}? {num1 != num2}")

#Mayor que (>)
print(f"¿El número {num1} es mayor que {num2}? {num1 > num2}")

#Menor que (<)
print(f"¿El número {num1} es menor que {num2}? {num1 < num2}")

#Mayor o igual que (>=)
print(f"¿El número {num1} es mayor o igual que {num2}? {num1 >= num2}")

#Menor o igual que (<=)
print(f"¿El número {num1} es menor o igual que {num2}? {num1 <= num2}")

#Operadores lógicos
a = True
b = False
c = True

#NOT (negación)
print(f"El resultado de NOT {a} es: {not a}")
print(f"El resultado de NOT {b} es: {not b}")

#AND (conjunción)
print(f"El resultado de {a} AND {b} es: {a and b}")
print(f"El resultado de {a} AND {c} es: {a and c}")

#OR (disyunción)
print(f"El resultado de {a} OR {b} es: {a or b}")
print(f"El resultado de {b} OR {b} es: {b or b}")
print(f"El resultado de {a} OR {c} es: {a or c}") 