#funcion de celsi a faren...

def clima(n):
    resultado = (n*9/5)+32
    return (resultado)

dato=float(input("ingrese la temperatura en celsius: "))
print("temperatura en fahrenheit: ",clima(dato))



#string
palabra=input("Ingresa una palabra: ").lower()
palabra_invertida=palabra[::-1]
print(palabra_invertida)



#numero_primo
def n_primos(n):
    if n <2:
        return ("no es primo")

    for i in range(2, n):
        if n % i == 0:
            return ("no es primo")

    return ("Es primo")

numero=int(input("Ingresa un numero: "))
print(n_primos(numero))




#crear_una_funcion
def mayor (a,b):
    return max(a,b)

dato_1 = int(input("Ingresa un numero: "))
dato_2 = int(input("Ingresa otro numero: "))
print ("El numero mayor es ",mayor(dato_1,dato_2))



#type_error
def division (a, b):
    return a // b

try:
    divisor=int(input("Ingrese el divisor: "))
    dividendo = int(input("Ingrese el dividendo: "))
    print(division(divisor, dividendo))
except ZeroDivisionError:
    print("No se puede dividir por 0")




#area de un rectangulo
def area (a,b):
    return a*b
base=int(input("Ingrese la base del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))
print("El area del rectangulo es: ",area(base,altura))