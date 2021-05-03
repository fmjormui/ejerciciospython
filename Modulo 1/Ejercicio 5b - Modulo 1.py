#Un usuario ingresa 3 números: Encontrar el mayor.

print("A continuación ingrese 3 números.")
numero1 = float(input("Ingrese su primer número: "))
numero2 = float(input("Ingrese su segundo número: "))
numero3 = float(input("Ingrese su tercer número: "))
if (numero1 > numero2 and numero1 > numero3):
    print("El primer número ({}) es el mayor".format(numero1))
else:
    if numero2 > numero3:
        print("El segundo número ({}) es el mayor".format(numero2))
    else:
        print("El tercer número ({}) es el mayor".format(numero3))
        if (numero3 % 2 == 0):
            print("Y además es par.")
        else:
            print("Es impar.")