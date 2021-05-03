#9. Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3.
#Internacional y la duración en minutos de la misma. Si el minuto cuesta $0.25
#para la llamada local, $0.40 para la llamada interurbana y $1.05 para la
#llamada internacional, diseñar un algoritmo que permita calcular el monto a
#pagar por dicha llamada.

llamada = int(input("Ingrese qué tipo de llamada desea realizar: (1) Local, (2) Interurbana o (3) Internacional: "))
duracion = int(input("Ingrese la cantidad de minutos: "))
if (llamada == 1):
    pagar = 0.25 * duracion
    print("Total a pagar: ${}.".format(pagar))
elif (llamada == 2):
    pagar = 0.40 * duracion
    print("Total a pagar: ${}.".format(pagar))
else:
    pagar = 1.05 * duracion
    print("Total a pagar: ${}.".format(pagar))