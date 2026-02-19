print("Calculadora".center(50, "-"))
print("º += suma \t "
      "º -: resta\t"
      "º  /: division\t"
      "º  *: multiplicación")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def division(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "No se puede dividir por cero"

def multiplicacion(a, b):
    return a * b

try:
    num_a = float(input("Ingrese un número: ".ljust(70)))
    operacion = input("Ingrese el símbolo de la operación que desea realizar: ".ljust(70))

    if operacion in ["+", "-", "*", "/"]:
        num_b = float(input("Ingrese otro número:".ljust(70)))
        if operacion == "+":
            print(suma(num_a, num_b))
        elif operacion == "-":
            print(resta(num_a, num_b))
        elif operacion == "/":
            print(division(num_a, num_b))
        elif operacion == "*":
            print(multiplicacion(num_a, num_b))
    else:
        print("Error: Operación no válida.")
except ValueError:
    print("Error: Debes ingresar un número válido.")




