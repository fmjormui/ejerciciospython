#4) Leer el número de mes y mostrar cuantos días tiene ese mes (año actual)


"""Revisar si hay una forma más sencilla de hacerlo"""
mes = 1
while (mes <= 12 and mes >= 1):
    mes = int(input("Ingrese el número del mes del que quiere saber cuántos días tiene: "))
    if (mes == 1):
        print("Enero tiene 31 días")
    elif (mes == 2):
        print("Febrero tiene 28 días")
    elif (mes == 3):
        print("Marzo tiene 31 días")
    elif (mes == 4):
        print("Abril tiene 30 días")
    elif (mes == 5):
        print("Mayo tiene 31 días")
    elif (mes == 6):
        print("Junio tiene 30 días")
    elif (mes == 7):
        print("Julio tiene 31 días")
    elif (mes == 8):
        print("Agosto tiene 31 días")
    elif (mes == 9):
        print("Septiembre tiene 30 días")
    elif (mes == 10):
        print("Octubre tiene 31 días")
    elif (mes == 11):
        print("Noviembre tiene 30 días")
    elif (mes == 12):
        print("Diciembre tiene 31 días")
    else:
        print("Ese número no corresponde a un mes.")