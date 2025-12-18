#Desarrolla un programa que pida al usuario una cadena de texto y cuente cuantas vocales, consonantes y espacios contiene, mostrando cada uno por separado.
texto=input("Ingrese una cadena de texto: ")

vocales="aeiouAEIOU"
contador_vocales=0
contador_consonantes=0
contador_espacios=0

for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter == " ":
        contador_espacios += 1
    
    else:
        contador_consonantes += 1
print(f"El texto ingresado contiene: {contador_vocales} vocales, {contador_consonantes} consonantes y {contador_espacios} espacios.")
