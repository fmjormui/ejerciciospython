#1) Calcular el promedio semanal de gastos en un mes, ingresando como datos:
#    Semana número
#    Gasto semanal
#El proceso termina cuando “semana número” es igual a 5.

semana = 1
gastoTotal = 0

while (semana < 5):
    semana = int(input(("Ingrese número de semana (1 a 4): ")))
    gasto = float(input(("Ingreso el gasto semanal: $")))
    gastoTotal = gastoTotal + gasto
    semana = semana + 1
print("Su gasto promedio fue de ${}".format(gastoTotal / 4))
