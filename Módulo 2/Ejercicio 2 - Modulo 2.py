#2) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

numero = 1
numerosPositivos = 0
while (numero != 0):
    numero =float(input("Ingrese un número: "))
    if (numero > 0):
        numerosPositivos = numerosPositivos + 1
print("La cantidad de numeros positivos es {}.".format(numerosPositivos))