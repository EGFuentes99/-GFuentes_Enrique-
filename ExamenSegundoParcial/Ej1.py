def calcular_promedio_semanal():
    temperaturas = []
    for i in range (7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
        promedio = sum(temperaturas) / len(temperaturas)
    print(f"La temperatura promedio semanal es: {promedio:.2f}°C")
calcular_promedio_semanal()