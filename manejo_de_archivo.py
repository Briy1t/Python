"""🔹 Conceptos Clave sobre Manejo de Archivos en Python
📌 ¿Por qué es importante? ✔ Permite leer, escribir y modificar archivos para almacenar datos
. ✔ Se usa en bases de datos, análisis de datos,
automatización y más.

📌 Modos de apertura (open()) ✔ "r" → Solo lectura.
✔ "w" → Escritura (borra contenido previo). ✔ "a" →
Agregar contenido sin borrar lo anterior. ✔ "r+"
→ Lectura y escritura combinadas.

📌 Métodos comunes ✔ read() → Lee todo el contenido
del archivo. ✔ readline() → Lee una línea a la vez.
✔ write() → Escribe en el archivo. ✔ close() →
Cierra el archivo después de usarlo.

📌 Archivos CSV ✔
Se usan para almacenar datos en formato tabular
. ✔ Se pueden leer con csv.reader() y escribir con csv.writer()."""

"""file=open('creacion_de_texto.txt','r')
print(file)
lineas=file.readlines()
print(lineas)
file.close() # es necesaerio cerrar es una buena practica
"""

"""with open('creacion_de_texto.txt', 'r') as archivo: # with lo toma como archivo y no es necesaerio cerrarlo
    lineas = archivo.readlines()
    print(lineas)

print(lineas)# aunque esta fuera se puede usar la variable

for l in lineas: # para reemplazar los espacios
    print(l.replace('\n', ' '))"""

"""with open('creacion_de_texto.txt', 'r') as archivo:# vammos a imprimirlo sin los simbolos de linea
    contenido = archivo.read()
    lineas = contenido.split('\n')
    print(lineas)"""

"""with open('creacion_de_texto.txt', 'r') as archivo:
    contenido = archivo.read()
    lineas = contenido.split('\n')
    pos=archivo.tell()
    print(pos)# lea la pocision en la que esta"""
