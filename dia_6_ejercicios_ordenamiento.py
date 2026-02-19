"""📅 Siguiente tema: Día 6 - Algoritmos y Estructuras de Datos (4h)
Objetivo: Aprender a optimizar código, comprender algoritmos de ordenamiento y búsqueda, y mejorar el rendimiento de las estructuras de datos.

📌 Conceptos clave
🔹 Algoritmos de ordenamiento (bubble sort, quick sort). 🔹 Algoritmos de búsqueda (búsqueda lineal, búsqueda binaria). 🔹 Eficiencia del código (Big-O notation).

📖 Enlaces de referencia: 🔗 Algoritmos en Python - GeeksforGeeks 🔗 Estructuras de datos - Python Docs"""
"""bubble sort no es usado es muy ineficiente """

"""📖 Ejemplo de Bubble Sort
Lista desordenada:"""

num_list=[10,20,35,2,4,8,0,34,11]

for num in num_list:
    print (num)




Lista = [2, 5, 8, 12, 16, 23, 38, 56, 72]

def busqueda_binaria(lista, objeto, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == objeto:
        return medio
    elif objeto < lista[medio]:
        return busqueda_binaria(lista, objeto, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objeto, medio + 1, fin)

# Llamada a la función con los índices de inicio y fin
print(busqueda_binaria(Lista, 23, 0, len(Lista) - 1))




num_list=[10,20,35,2,4,8,0,34,11]

def bubble_sort(lista):
    n=len(lista)#cantidad de elementos en la lista

    for i in range (n): #recorre la lista varias veces
        for j in range (n-1):# recorrer los elementos
            if lista[j]>lista[j+1]:# haci se compoaran dos elementos vecinos
                lista[j], lista[j+1]=lista[j+1],lista[j] #intercambian valores
    return lista
print(bubble_sort(num_list))

"""quick sort : divide y venceras requiere de mas tiempo y 
ordena de izquierda a derecha"""

def quick_sort(lista):
    n=len(lista)
    if n<=1: return lista
    pivote=lista[0]
    menores=[n for n in lista if n < pivote ]
    mayores=[n for n in lista if n > pivote]
    return quick_sort(menores)+[pivote]+ quick_sort(mayores)
print(quick_sort(num_list))

def busqueda_binaria (lista, objeto):#caso base si la lista esta vacia
    if len(lista)==0:
        return -1

    medio = len(lista)//2# posicion centrada
    if lista[medio] ==objeto: # si el objeto esta en posicion central
        return medio
    elif objeto< lista[medio]: #si el objeto es menor
        return busqueda_binaria(lista[:medio],objeto)
    else:
        return busqueda_binaria(lista[medio +1:],objeto)

num_list = [2, 4, 8, 10, 11, 20, 34, 35]
print(busqueda_binaria(num_list, 10))  # Debería devolver la posición del número 10
print(busqueda_binaria(num_list, 100))