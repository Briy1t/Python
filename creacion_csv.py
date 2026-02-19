import csv
import os

ruta = "agendatelefonica.csv"

if os.path.exists(ruta):
    print(f"El archivo '{ruta}' ha sido creado exitosamente.")
else:
    print(f"El archivo '{ruta}' no se encuentra en la carpeta del proyecto.")

with open("agendatelefonica.csv", "a", newline= "") as archivo:
    escritor_csv=csv.writer(archivo)

    nombre= input("Nombre de contacto:  ")
    telefono= input("Numero de contacto:  ")

    escritor_csv.writerow([nombre,telefono])
    print("se ha guardado en la agenda el contacto: ",nombre," con el telefono",telefono)

