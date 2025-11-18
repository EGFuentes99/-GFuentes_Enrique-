#Ejercicio 1: Haz un programa que pida una frase, divídela en palabras y guarda una lista solo las palabras que tengan más de 5 letras. Muestra la lista resultante.
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_mas_de_5_letras = []
for palabra in palabras:
    if len(palabra) > 5:
        palabras_mas_de_5_letras.append(palabra)
print("Palabras con más de 5 letras:", palabras_mas_de_5_letras)    

#Ejercicio 2: Haz un programa que pida una frase y cuenta cuántas veces aparece cada palabra. Por ejemplo "Esta es una prueba", "Esta" aparece una vez, "es", una vez, "una", una vez, etc...
frase = input("Ingrese una frase: ")
palabras = frase.split()
conteo_palabras = {}
for palabra in palabras:
    palabra = palabra.lower()  
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
for palabra, conteo in conteo_palabras.items():
    print(f"La palabra '{palabra}' aparece {conteo} veces.")    

#Ejercicio 3: Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
contraseña = input("Ingrese una contraseña: ")
tiene_mayuscula = False
tiene_numero = False

if len(contraseña) >= 8:
    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        if char.isdigit():
            tiene_numero = True
    if tiene_mayuscula and tiene_numero:
        print("Contraseña válida.")
    else:
        print("La contraseña debe contener al menos una letra mayúscula y un número.")
else:
    print("La contraseña debe tener al menos 8 caracteres.")

#Ejercicio 4: Haz un programa que pida un texto y una palabra. Si la palabra está en el texto, muestra cuántas veces aparece.
texto = input("Ingrese un texto: ")
palabra = input("Ingrese una palabra a buscar: ")
texto_formateado = texto.lower()
palabra_formateada = palabra.lower()
conteo = texto_formateado.count(palabra_formateada)
print(f"La palabra '{palabra}' aparece {conteo} veces en el texto.")

#Ejercicio 5: Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla.
lista_palabras = input("Ingrese una lista de palabras separadas por comas: ")
palabras = lista_palabras.split(",")
palabras_filtradas = set()
for palabra in palabras:
    palabra = palabra.strip()
    if len(palabra) >= 3:
        palabras_filtradas.add(palabra) 

nueva_lista = list(palabras_filtradas)
print("Nueva lista de palabras:", nueva_lista)

#Ejercicio 6: Crea un diccionario con clave y valor producto : precio. Luego, pide una lista de productos comprados y muestra el total de la compra. Si el producto no existe, muestra una advertencia.
diccionario_productos = {
    "manzanas": 10,  
    "bananas": 5,
    "naranjas": 8,
    "peras": 12,
    "uvas": 15
}
productos_comprados = input("Ingrese una lista de productos comprados separados por comas: ")
productos = productos_comprados.split(",")
total_compra = 0
for producto in productos:
    producto = producto.strip().lower()
    if producto in diccionario_productos:
        total_compra += diccionario_productos[producto]
    else:
        print(f"Advertencia: El producto '{producto}' no existe en el diccionario.")
print(f"El total de la compra es: {total_compra}")

#Ejercicio 7: Haz un programa que pida repetidamente el nombre de una persona y su respuesta ("Si" o "No"). Guarda cada respuesta en un diccionario, donde la clave sea el nombre, y el valor sea la respuesta. El programa debe terminar cuando el usuario escriba "Fin" como nombre. Al finalizar, muestra cuántas personas respondieron "Si" y cuántas "No".
respuestas = {}
while True:
    nombre = input("Ingrese el nombre de una persona (o 'Fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    respuesta = input("Ingrese la respuesta (Si/No): ")
    respuestas[nombre] = respuesta
conteo_si = sum(1 for resp in respuestas.values() if resp.lower() == "si")
conteo_no = sum(1 for resp in respuestas.values() if resp.lower() == "no")
print(f"Cantidad de respuestas 'Si': {conteo_si}")
print(f"Cantidad de respuestas 'No': {conteo_no}")

#Ejercicio 8: Haz un programa que pida una palabra y verifique si inicia con una vocal.
palabra = input("Ingrese una palabra: ")
if palabra[0].lower() in 'aeiou':
    print("La palabra inicia con una vocal.")
else:
    print("La palabra no inicia con una vocal.")


#Ejercicio 9: Haz un programa que pida el nombre de un contacto y su teléfono, y los agregue a un diccionario.
contactos = {}
nombre = input("Ingrese el nombre del contacto: ")
telefono = input("Ingrese el teléfono del contacto: ")
contactos[nombre] = telefono
print("Contacto agregado:", contactos)


#Ejercicio 10: Haz un programa que pida 5 nombres y luego pregunte uno; si está en la lista, muestra "Encontrado".
nombres = []
for _ in range(5):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
nombre_a_buscar = input("Ingrese un nombre para buscar: ")
if nombre_a_buscar in nombres:
    print("Encontrado") 
else:
    print("No encontrado")