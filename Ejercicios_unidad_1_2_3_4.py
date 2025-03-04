
a= "Sara"
b= 2
c= 4+3j
d= 2==2
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#tipos datos
nombre = input("¿cual es tu nombre?")
edad = input("¿cual es tu edad?")
print( "Hola", nombre, "tienes", edad, "años." )
#area y perimetro rectangulo
altura=int(input("Ingrese la altura"))
base=int(input("Ingrese la base"))
area=altura*base
print(area)
#par o impar
numero=int(input("Ingrese un numero"))
if numero %2==0:
    print("El numero es par")
else:
    print("El numero es impar")
#convertidor
#conversor de moneda
taza=float(input("Ingrese la cantidad de dolares que tiene: "))
euro=1.062
dolar=0.95575
operacion=dolar/euro
cambio=operacion*taza
print("el cambio son",(cambio), "euros:")
#condicionales
#mayor o menor de edad
usuario=int(input("ingrese su edad"))
if usuario <18 :
    print("el usuario es menor de edad ")
elif usuario > 60:
    print("el usuario es adulto mayor")
else:
  print("el usuario es mayor de edad ")
#positivo negativo cero
numero=int(input("ingrese un numero"))
if numero >0:
    print("el numero es positivo")
elif numero ==0:
    print("el numero es cero")
else:
    print("el numero es negativo")
#numero aleatorio
import random
numero_aleatorio= random.randint(1,10)
while True:
  numero=int(input("ingrese un numero"))
  if numero_aleatorio== numero:
    print("Felicidades")
    break
  else:
    print("el numero es incorrecto")
#for
for x in range(1,11):
    print(x)
#otra opcion
for x in range(1, 11):
    print(f"Este es el número {x}")
#numero 0
while True:
    numero = int(input("Ingresa un numero"))
    if numero==0:
        print("felicidades")
        break
    else:
        print("sigue intentando")
# dia 3
#se puede repetir la funcion
def saludar():
    print("hola mundo")

saludar()