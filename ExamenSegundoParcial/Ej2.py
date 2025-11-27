#Haz un programa que solicite una oración y reemplaza todas las letras a, i, u por el caracter "#"
def reemplazar_vocales():
    oracion = input("Ingrese una oración: ")
    oracion_modificada = oracion.replace('a', '#').replace('i', '#').replace('u', '#')
    print("Oración actualizada:", oracion_modificada)
reemplazar_vocales()