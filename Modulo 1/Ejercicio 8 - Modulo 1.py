#8. Calcular el importe que debe pagar un auto en un estacionamiento
#teniendo en cuenta como datos las horas y minutos de uso. El valor de la hora
#es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. El
#mínimo a cobrar es de una hora.

horas = int((input("Ingrese las horas de uso del estacionamiento: ")))
minutos = int((input("Ingrese los minutos de uso del estacionamiento: ")))
if ((minutos < 15) and (horas > 0)):
    total_cobrar = (horas * 45)
    print("El total a cobrar es ${}.".format(total_cobrar))
elif (minutos > 15):
    total_cobrar = (horas * 45) + 45
    print("El total a cobrar es ${}.".format(total_cobrar))
else:
    print("El total a cobrar es $45.")