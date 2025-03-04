def suma(a, b):
    return a + b
resultado=suma(6, 8)
print(resultado)

"""
#area
altura=float(input("Ingresa la altura del rectangulo"))
base=float(input("Ingresa la base a del rectangulo"))
area=(altura*base)
print("El area del rectangulo es:",area,"cm")
#perimetro
perimetro=(altura+base*2)
print("perimetro del rectangulo es:",perimetro,"cm")
"""

def perimetro_rectangulo(base, altura):
    perimetro = (base + altura) * 2
    print("El perímetro del rectangulo es:",perimetro,"cm")





if __name__ == '__main__':
    perimetro_rectangulo(100, 50)
    print(len(["Pepe", 1, (2,2)]))
