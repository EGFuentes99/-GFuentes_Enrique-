#Pide al usuario ingresar 5 precios (Se aceptan con punto decmal), guárdalos en una lista y calcula el total. Si el total supera $500, muestra "Compra alta", si es menor muestra "Compra baja", si todos los productos son mayores a $100, muestra "Productos premium".
def analizar_precios():
    precios = []
    for i in range(5):
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        precios.append(precio)
    
    total = sum(precios)
    print(f"El total de la compra es: ${total:.2f}")
    
    if total > 500:
        print("Compra alta")
    else:
        print("Compra baja")
    
    if all(precio > 100 for precio in precios):
        print("Productos premium")

analizar_precios()