#Solicita el nombre de 5 animales. Guárdalos en un arreglo y muestra solo aquellos cuyos nombres comiencen con una vocal
def filtrar_animales_por_vocal():
    animales = []
    for i in range(5):
        animal = input(f"Ingrese el nombre del animal {i+1}: ")
        animales.append(animal)

    animales_con_vocal = [animal for animal in animales if animal[0].lower() in 'aeiou']

    print("Animales cuyos nombres comienzan con una vocal:")
    for animal in animales_con_vocal:
        print(animal)

filtrar_animales_por_vocal()
