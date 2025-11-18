#Funciones en Python

#Definición 
def saludar():
    print("Hola, bienvenido a la clase de Python")

    #Llamada a la función saludar
saludar()

#Funciones con parámetros
def saludar_persona(nombre, apellido, edad):
    print(f"Hola {nombre} {apellido}, tienes {edad} años.")

#Llamada a la función con argumentos
saludar_persona("Enrique", "Guzmán", 26) 
saludar_persona("Ana", "Banana", 26)
saludar_persona("Mónica", "Gonzalez", 22)

#Funciones con valor de retorno
def sumar(a, b):
    return a + b

print(sumar(5, 10))
resultado = sumar(15, 25)
print(f"El resultado de la suma es: {resultado}")

