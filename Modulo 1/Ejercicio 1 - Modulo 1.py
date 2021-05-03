#1. Calcular el sueldo de una persona, conociendo la cantidad de horas
#que trabaja en el mes y el valor de la hora.

horas = (float(input("Ingrese las horas que trabaja: ")))
valor_hora = (float(input("Ingrese el valor de la hora:")))
sueldo = (horas + valor_hora)
print("Usted cobra: $" + str(sueldo))