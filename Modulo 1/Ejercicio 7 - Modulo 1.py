#7. Ingresar dos números, calcular y mostrar el cociente del primero por el
#segundo, siempre que el divisor no sea cero. En este último caso mostrar la
#leyenda “no se puede realizar el cociente”. 

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))
if (numero2 == 0):
    print("No se puede realizar el cociente.")
else:
    cociente = numero1 / numero2
    print(cociente)