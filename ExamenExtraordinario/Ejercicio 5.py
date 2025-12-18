#Crea un programa que pida un numero entero y muestre la tabla de multiplicar de ese numero del 1 al 10.
numero_usuario = int(input("Introduce un numero entero: "))
print(f"Tabla de multiplicar del {numero_usuario}: ")
for i in range(1, 11):
    print(f"{numero_usuario} x {i} = {numero_usuario * i}")