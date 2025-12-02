#En Python existen los siguientes modos de escritura y lectura de archivos:
#'r' - Modo de lectura (read): Este es el modo predeterminado. Abre un archivo para leer su contenido. Si el archivo no existe, se genera un error.
#'w' - Modo de escritura (write): Abre un archivo para escribir en él. Si el archivo ya existe, su contenido se borra. Si el archivo no existe, se crea uno nuevo.
#'a' - Modo de anexado (append): Abre un archivo para agregar contenido al final del mismo. Si el archivo no existe, se crea uno nuevo.
#'r+' - Modo de lectura y escritura (read and write): Abre un archivo para leer y escribir en él. El archivo debe existir; de lo contrario, se genera un error.
#'w+' - Modo de escritura y lectura (write and read): Abre un archivo para escribir y leer. Si el archivo ya existe, su contenido se borra. Si el archivo no existe, se crea uno nuevo.
#'a+' - Modo de anexado y lectura (append and read): Abre un archivo para agregar contenido al final y leerlo. Si el archivo no existe, se crea uno nuevo.


#Apertura de archivo
#Open("ruta/archivo.txt", "modo")

#Cerrar el archivo
#archivo.close()

#Podemos abrir el archivo haciendo uso de (with) para que se cierre el archivo automáticamente al finalizar el bloque de código
#with open("ruta/archivo.txt", "modo") as archivo:
    #Operaciones con el archivo

with open("Clase 13.txt", "r") as f:
    contenido = f.read() #Lee todo el contenido del archivo y lo va a almacenar en la variable contenido
print(contenido) #Imprime el contenido del archivo 

with open("Clase 13.txt", "r") as f:
    for linea in f: #Lee el archivo línea por línea
        print(linea.strip()) #Imprime cada línea sin espacios adicionales al inicio o al final

with open("Clase 13.txt", "w") as f:
    f.write("Esta es una nueva línea escrita en el archivo.\n") 
    f.write("Otra línea añadida al archivo.\n")

with open("Clase 13.txt", "a") as f:
    f.write("Esta línea se añade al final del archivo.\n")

with open("Clase 13.txt", "r+") as f:
    contenido = f.read()
    f.write("\nEsta línea se añade después de leer el contenido.\n")

with open("Clase 13.txt", "w+") as f:
    f.write("Escribiendo en archivo2 uwando W+.\n")
    f.seek(0)  # Mover el cursor al inicio del archivo para leer lo que acabamos de escribir
    contenido = f.read()
    print(contenido)

with open("Clase 13.txt", "a+") as f:
    f.write("Añadiendo una línea usando A+.\n")
    f.seek(0)  #Volver al inicio del archivo para leer todo el contenido")
    contenido = f.read()
    print(contenido)

