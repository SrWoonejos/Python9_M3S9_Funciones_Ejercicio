def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Diccionario
def calcular_operaciones(a, b):
    resultados = {
        "Suma": sumar(a, b),
        "Resta": restar(a, b),
        "Multiplicación": multiplicar(a, b),
        "División": dividir(a, b)
    }

    return resultados  

#Usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

#Función que calcula las operaciones
resultados = calcular_operaciones(num1, num2)

# Imprimir
for operacion, resultado in resultados.items():
    print(f"{operacion}: {resultado}")
