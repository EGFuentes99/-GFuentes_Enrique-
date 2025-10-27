#Ejercicio 1_ Haz un programa que solicite al ususario ingresar 5 calificaciones y calcula el promedio

#Solicitar al usuario ingresar las 5 calificaciones
califiacion1 = Float(input("Ingresa la calificación 1: "))
califiacion2 = Float(input("Ingresa la calificación 2: "))
califiacion3 = Float(input("Ingresa la calificación 3: "))
califiacion4 = Float(input("Ingresa la calificación 4: "))
califiacion5 = Float(input("Ingresa la calificación 5: "))

#Calcular el promedio
promedio = (califiacion1 + califiacion2 + califiacion3 + califiacion4 + califiacion5) / 5

#Mostrar el promedio
print("El promedio de las calificaciones es:", promedio)