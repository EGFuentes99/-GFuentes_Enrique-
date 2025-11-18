nombre = "Enrique Javier Guzmán Fuentes"
cadena2 = "Hola motherfuckers, ¿cómo están? además de mongoles"
cadena3 = "    Santiago sale a kgar como 6 veces al día     "

print(len(nombre)) #Imprime la longitud de la cadena

print(nombre.upper()) #Convierte la canena a mayúsculas

print(nombre.lower()) #Convierte la canena a minúsculas

print(cadena2.capitalize()) #Convierte el primer caracter a mayúscula y el resto a minúsculas

print(cadena2.title()) #Convierte la primera letra de cada palabra a mayúscula

print(cadena3.strip()) #Elimina los espacios en blanco al inicio y al final de la cadena

cadenaNueva = cadena4 + cadena5
print(cadenaNueva) #Concatenación de dos cadenas o suma/unión de cadenas en una sola

cadenaMultiplicada = cadena4 * 5
print(cadenaMultiplicada) #Multiplicación de cadenas (repetición de la cadena un número determinado de veces)

print(cadena4.replace("a", "s")) #Reemplaza todas las apariciones de "a" por "s" en la cadena

cadena6 = "Tengo un chingo de frío y hambre"
indice = cadena6.find("frío") #Busca la posición de la subcadena "frío" en la cadena6
print(indiceUltimo) #Imprime laposición de la última aparición de "frío"

cadena7 = "Anita lava la tina"
conteo = cadena7.count("a") #Cuenta cuántas veces aparece la letra "a" en la cadena7
print(conteo) #Imprime el conteo de apariciones de "a"

print(cadena7.startswith("Anita")) #Verifica si la cadena7 comienza con "Anita"
print(cadena7.endswith("tina")) #Verifica si la cadena7 termina con "tina"

# Sintaxis de Slicing cadena[inicio:fin:paso]
cadena8 = "Hola a todos"
print(cadena8[0:4]) # Imprime "Hola"
print(cadena8[:4]) # Imprime "Hola"
print(cadena8[4:9]) # Imprime "a to"
print(cadena8[5:]) # Imprime "a todos"
print(cadena8[-2:]) # Imprime "os"
print(cadena8[::2]) # Imprime "Hl atds"
print(cadena8[::-1]) # Imprime la cadena al reves "sodot a aloH"

#Ejercicio 1: Pide una frase y muestra la misma frase sin espacios al inicio y al final con todas las letras en minuscula
frase = input("Escribe una frase: ")
fraseLimpia = frase.strip().lower()
print(fraseLimpia)

#Ejercicio 2: Pide una palabra y comprueba si es un palíndromo
palabra = input("Escribe una palabra: ")
palabra_invertida = palabra[::-1]
if palabra.lower() == palabra_invertida.lower():
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

