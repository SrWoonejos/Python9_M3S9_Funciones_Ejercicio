# area rectangulo
def area_rectangulo(base, altura):
     area = base * altura
     return area

#bucle para nro positivo
def nro_positivo(msje):
    while True:
         try:
              nro = float(input(msje))
              if nro > 0:
                   return nro
              else:
                   print("Solo debes ingresar números positivos. Inténtalo de nuevo!")
         except ValueError:
              print("Ingresa solo números positivos")

#Usuario ingresa variables
base = nro_positivo("Ingresa la base del rectángulo")
altura = nro_positivo("Ingresa la altura del rectángulo")

#Calculo
resultado = area_rectangulo(base, altura)
print(f"El área es: {resultado}")