#7) Ingresar las temperaturas registradas a distintas horas de un día en grados hasta que
#ésta sea 100. Mostrar la temperatura máxima y la temperatura mínima.

"""Revisar como poner máximos y mínimos"""
temperatura = 0
temperaturaTotal = 0
while (temperatura < 100):
    temperatura = int(input("Ingrese la temperatura: "))
    print("Hubo {}°C.".format(temperatura))
    temperaturaTotal = temperaturaTotal + temperatura
    if (temperaturaTotal == 100):
        print("La temperatura máxima fue de {}".format(sys.maxsize(temperatura)))
        print("La temperatura mínima fue de {}".format(min(temperatura)))
