#area
altura=float(input("Ingresa la altura del rectangulo"))
base=float(input("Ingresa la base a del rectangulo"))
area=(altura*base)
print("El area del rectangulo es:",area,"cm")
#perimetro
perimetro=(altura+base*2)
print("perimetro del rectangulo es:",perimetro,"cm")
#numneroparroimpar
numero=int(input("Ingresa un numero"))
if numero%2==0:
    print("El numero es par")
else:
    print("El numero es impar")
#conversor de temperatura
celsius=int(input("Ingresa el clima en grados Celsius: "))
faherheit=(celsius*9/5+32)
print("grados Fahrenheit",faherheit)
#Area_de_un_circulo
#Area_de_un_circulo: fue necesario importar math.pi
import math
diametro=float(input("Ingresa el diametro del circulo"))
radio=diametro/2
area= math.pi * (radio **2)
print("la area es: ",area)
#comparacion de nuemros
numero_1=float(input("Ingresa un numero: "))
numero_2=float(input("Ingresa un numero: "))

if numero_1>numero_2:
    print("El numero",numero_1,"es mayor que el numero: ",numero_2)
elif numero_2>numero_1:
    print("El numero",numero_2,"es mayor que el numero: ",numero_1)
else:
    print("los numeros",numero_1,"y", numero_2,"son iguales")
#calculadora basica
numero_1=float(input("Ingresa un numero: "))
numero_2=float(input("Ingresa un numero: "))
suma=numero_1+numero_2
print("Resultado de suma",suma)
restar=numero_1-numero_2
print("Resultado de restar",restar)
multiplicacion=numero_1*numero_2
print("Resultado de multiplicacion",multiplicacion)
division=numero_1/numero_2
print("Resultado de division",division)
#determine si un numero es negativo positivo o cero
numero=int(input("Ingresa un numero"))
if numero<0:
    print("El numero",numero,"es negativo")
elif numero==0:
    print("El numero",numero,"es cero")
else:
    print("El numero",numero,"es positivo")
#Calculo de descuento
descuento=floar(input("Ingresa el precio"))

