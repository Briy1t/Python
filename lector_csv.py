import csv

# Leer un archivo CSV
with open("contactos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila del archivo
