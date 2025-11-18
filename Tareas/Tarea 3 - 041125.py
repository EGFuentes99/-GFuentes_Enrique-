# #Ejercicio 1: Haz un programa que calcule cuantos números del 1 al 100 son divisibles entre el 3 y el 5
conteo_visibles = 0
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        conteo_visibles += 1
print(f"Hay {conteo_visibles} números entre 1 y 100 que son divisibles entre 3 y 5.")

# #Ejercicio 2: Haz un programa que solicite números al usuario hasta que ingrese un cero. Al final, imprime cuántos números positivos y negativos introdujo
numeros_positivos = 0
numeros_negativos = 0
while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    elif numero > 0:
        numeros_positivos += 1
    else:
        numeros_negativos += 1
print(f"Números positivos ingresados: {numeros_positivos}")
print(f"Números negativos ingresados: {numeros_negativos}")

# #Ejercicio 3: Haz un programa que pida un número y muestre si es divisible entre 2, 3 o ambos
numero = int(input("ingrese un número: "))
if numero % 2 == 0 and numero % 3 == 0:
    print(f"El número {numero} es divisible entre 2 y 3.")
elif numero % 2 == 0:
    print(f"El número {numero} es divisible entre 2.")
elif numero % 3 == 0:
    print(f"El número {numero} es divisible entre 3.")
else:
    print(f"El número {numero} no es divisible entre 2 ni 3.")

# #Ejercicio 4: Haz un programa que sume todos los numeros impares del 1 al 50
suma_impares = 0 
for numero in range(1, 51):
    if numero % 2 != 0:
        suma_impares += numero
print(f"La suma de todos los números impares del 1 al 50 es: {suma_impares}.")

# #Ejercicio 5: Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría: Menor de 13 años -> "Niño", 13 a 17 años -> "Adolescente", 18 a 64 años -> "Adulto", 65 o más -> "Adulto mayor"
edad = input("Ingrese su edad: ")
edad = int(edad)
if edad < 13:
    categoria = "Niño"
elif 13 <= edad <= 17:
    categoria = "Adolescente"
elif 18 <= edad <= 64:
    categoria = "Adulto"   
else:
    categoria = "Adulto mayor"
print(f"Usted es un {categoria}.")  

#Ejercicio 6: Haz un programa que pida un número, y muestre si es primo o no
numero = int(input("Ingrese un número: "))
if numero <= 1:
    print(f"El número {numero} no es primo.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {numero} es un número primo.")
    else:
        print(f"El número {numero} no es un número primo.")

#Ejercicio 7: Haz un programa que pida un número, y calcule la suma de todos los números, desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5
numero = int(input("Ingrese un número: "))
suma_total = 0
for i in range(1, numero + 1):
    suma_total += i
print(f"La suma de todos los números desde 1 hasta {numero} es: {suma_total}.")

#Ejercicio 8: Pide dos números y muestra todos los números entre ellos que sean multiplos de 7
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Números múltiplos de 7 entre {num1} y {num2}:")
for numero in range(min(num1, num2), max(num1, num2) +  
1):
    if numero % 7 == 0:
        print(numero)

#Ejercicio 9: Pida una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%
cantidad_productos = int(input("Ingrese una cantidad de productos: "))
total_sin_iva = 0
for i in range(cantidad_productos):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    total_sin_iva += precio
iva = total_sin_iva * 0.16
total_con_iva = total_sin_iva + iva
print(f"El total con IVA del 16% es: {total_con_iva:.2f}")

#Ejercicio 10: Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir
while True:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    
    if opcion == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

        