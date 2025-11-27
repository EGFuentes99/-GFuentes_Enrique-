def ordenar_canciones_inverso():
    canciones = []
    for i in range(6):
        titulo: str = input(f"Ingrese el titulo de una canción {i+1}: ")
        canciones.append(titulo)
    canciones.sort(reverse=True)
    print("Canciones en orden alfabético inverso:")
    for cancion in canciones:
        print(cancion)
ordenar_canciones_inverso()
