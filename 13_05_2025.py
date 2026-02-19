"""Día 5: Funciones y Manejo de Errores en Python (3h)
En Python, *args y **kwargs son tipos de argumentos que permiten a las funciones manejar un número variable de argumentos.
 *args se utiliza para pasar argumentos posicionales (aquellos que se pasan sin una clave)
y **kwargs para pasar argumentos con nombre (aquellos que se pasan con una clave y un valor). """
def division (a,b):
    try:
        resultado=a/b
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir en Zero"


num_a=float(input("Ingrese de divisor: "))
num_b=float(input("Ingrese de dividendo: "))
print(division(num_a,num_b))









try:
    num=int(input("Ingrese un numero: "))
    print("Su numero es correcto")

except ValueError as Error:
    print("Error, no haz ingresado un numero ")

def num_mayor (lista):
    mayor=lista[0]

    for num in lista:
        if num> mayor:
            mayor=num

    return mayor# necesite de ayuda








def numero_primo ():
    num=int(input("Ingrese un numero: "))

    if num <2:
        print("No es numero primo ")
        return False

    for i in range(2,num):
        if num % i==0:
            print("No es numero primo")
            return False

    print("Es numero primo ")
    return True

print(numero_primo())








def grados_celcius_a_farengeit ():
    celcius=int(input("Ingrese la temperatura en grados Celsious: "))
    farengeit=(celcius * 9/5) + 32
    return farengeit

print(grados_celcius_a_farengeit())


def suma(a,b):
    return a+b
num_a=int(input("Ingrese un numero:\t"))
num_b=int(input("Ingrese un numero:\t"))
resultado=suma(num_a,num_b)
print(f"Su resultado es: {resultado} ")

