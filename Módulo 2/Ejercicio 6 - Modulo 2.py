#6) Leer dos números, mostrar el siguiente Menú pudiendo seleccionar alguna opción y
#repetir esta operación hasta que seleccione 5.
# Menú principal
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
# Seleccione una opción:

numero1 = 0
numero2 = 0
opcion = 1
while (opcion >= 1) and (opcion <= 4):
    numero1 = float(input("Ingrese un número: "))
    numero2 = float(input("Ingrese un segundo número: "))
    print("Menú principal")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    if (opcion == 1):
        suma = numero1 + numero2
        print("La suma entre ambos números es  igual a {}".format(suma))
    elif (opcion == 2):
        resta = numero1 - numero2
        print("La resta entre ambos números es  igual a {}".format(resta))
    elif (opcion == 3):
        multiplicacion = numero1 * numero2
        print("La multiplicación entre ambos números es  igual a {}".format(multiplicacion))
    elif (opcion == 4):
        if (numero2 != 0):
            division = numero1 / numero2
            print("La división entre ambos números es  igual a {}".format(division))
        else:
            print("No es posible dividir por cero.")
    else:
        print("Operación terminada.")
            