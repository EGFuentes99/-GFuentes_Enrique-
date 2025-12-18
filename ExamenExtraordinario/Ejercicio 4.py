#Desarrolle un programa que solicite al usuario una palabra y determine si es un palindromo (si se lee igual de izquierda a derecha que de derecha a izquierda).
palabra = input("Ingrese una palabra: ")
palabra_limpia = palabra.replace(" ", "").lower()
if palabra_limpia == palabra_limpia[::-1]:
    print(f"La palabra '{palabra}' es un palindromo.")
else:
    print(f"La palabra '{palabra}' no es un palindromo.")   
