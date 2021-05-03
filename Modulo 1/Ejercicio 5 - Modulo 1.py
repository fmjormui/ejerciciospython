#5. Ingresar un número. Si es positivo, calcular su raíz cuadrada, si es negativo mostrar su cuadrado y si es cero mostrar “Error. Ha ingresado un valor nulo”.

numero = int(input("Ingrese un número: "))
if (numero > 0):
    raiz_cuadrada = numero ** 0.5
    print("La raíz cuadrada del número {} es: {}".format(numero,raiz_cuadrada))
elif (numero < 0):
    cuadrado = numero ** 2
    print("El cuadrado del número {} es: {}".format(numero,cuadrado))
else:
    print("Error. Ha ingresado un valor nulo")