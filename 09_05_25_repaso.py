alumnos={ "Andres": 20 , "Camila": 23, "Leon": 21, "Sara": 19}

for nombre,edad in alumnos.items():
    print(f"Nombre es {nombre} su edad es {edad}")

print(f"La edad de camila es : {alumnos['Camila']}")# para sacar solo un dato

alumnos["Kevin"]=28#para añadir al diccionario
print(alumnos)
alumnos.update({"Dylan":22,"Amaranto":25})# para dos datos o mas
print(alumnos)

for indice,(nombre,edad) in enumerate (alumnos.items()):
    print(f"{indice + 1}. {nombre}-{edad} años")



colores=("rojo","amarillo","azul","violeta","verde")
for element in colores:
    print(element)
# la tupla no se puede modificar
colores_ordenados=sorted(colores)
print(colores_ordenados)

num=[3,7,2,8,99,4,1]
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)




numeros=[2,3,5,8,9]#lista
print(numeros)
numeros.append(0 ) #solo un numero si en este le pongo uno al lado ente ""  se vuelve una tupla
numeros.extend([2,7])# se pueden dos
#pop() sirve para eliminar un elemento de una lista y devolver dicho elemento
numeros.remove(3)



"""pedir numeros hasta que el usuario ingrese 0"""
print("Ingrese un numero\t")

while True:
    entrada=float(input(":\t"))
    if entrada== 0:
        print("Final del proceso")
        break
    else:
        print("Ingrese un numero")






contador=1 #donde empieza
rango=5 #hasta donde llega
while contador <=rango:# se ejecuta hasta que sea igual a 5
    print(contador)
    contador += 1 # el uno incrementa en numero




numeros=[1,2,6,7,10]
suma= 0
for num in numeros:
    suma += num
    print(suma)



nombres=["sara","andrea","carlos"]

for x in nombres:
    print(x)

def area_de_un_triangulo (base ,altura):
    return (base*altura)/2

# Solicitar datos al usuario
b = float(input("Ingrese la base del triángulo: "))
h = float(input("Ingrese la altura del triángulo: "))

# Llamar a la función y mostrar el resultado
print(f"El área del triángulo es: {area_de_un_triangulo(b, h)}")


for i in range (0,11):
    print(i)


print("Aprobo o Reprobo".center(50,"-"))

aprobo=6

entrada=int(input("Ingrese la calificacion:\t"))
if entrada >= aprobo:
    print("¡Felicidades Aprobaste!")
else :
    print("Has Reprobado")


print("suma de numeros".center(50,"_"))
def suma (a,b):
    resultado= a+b
    return resultado

num_1=int(input("Ingrese un numero: \t"))
num_2=int(input("Ingrese un numero: \t"))
solucion=suma(num_1,num_2)
print(f"Su resultado es: \t {solucion}")



"numero par e impar"
print("Numero Par o Impar ".center(50,"-"))

num_a=int(input("Ingrese su numero\t"))

if num_a %2==0:
    print("Es un numero par",num_a)
else:
    print("Es un numero impar ", num_a)

def es_par_o_impar (num):
    if num %2==0:
        return ("numero par")
    else:
        return ("numero impar")

entrada=int(input("ingrese un numero\t"))
numero=es_par_o_impar(entrada)
print(f"El numero {entrada} es {numero}")


























"""suma de numeros"""
titulo="SUMA DE NUMEROS"
print(titulo.center(50, "-"))

def suma (a,b):
    return a+b


num_a=int(input(f"ingrese su primer numero:".ljust(35)))
num_b=int(input(f"ingrese su segundo numero:".ljust(35)))

print(f"\n{'resultado:'.ljust(35)}{ suma(num_a,num_b)}")
