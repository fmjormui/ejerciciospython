#5) Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en
#número y letras.

"""Revisar cómo expresar en letras los números"""
numero = 0
dato = 5
while numero < 10:
    numero = numero + 1
    if (dato > 3) and (dato < 8):
        dato = float(input("Ingrese un número mayor a 3 y menor a 8: "))
        print(dato)