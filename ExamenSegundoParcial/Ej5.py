def analizar_precios():
    precios = []
    for i in range(5):
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        precios.append(precio)
    
    total = sum(precios)
    print(f"El total de la compra es: ${total:.2f}")
    
    if total > 500:
        print("Compra Alta")
    else:
        print("Compra Baja")
    
    if all(precio > 100 for precio in precios):
        print("Productos Premium")

analizar_precios()