#3) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo de cada curso:
#    Curso (1-5)
#    Presentes
#    Ausentes
#Calcular
#    Por cada curso el porcentaje de presentes sobre el total
#    Cantidad de ausentes en el colegio
#    Curso con mayor cantidad de ausente

"""Revisar si hay una forma más sencilla de hacerlo"""
curso = 0
totalAlumnos = 0
presentes = 0
porcPresentes = 0
ausentes1 = 0
ausentes2 = 0
ausentes3 = 0
ausentes4 = 0
ausentes5 = 0
ausentesTotal = 0
while (curso <= 5):
    curso = int(input(("Indique el número del curso: ")))
    curso = curso + 1
    if (curso == 2):
        totalAlumnos = int(input(("Indique el total de alumnos del curso: ")))
        presentes = int(input(("Indique cantidad de alumnos presentes: ")))
        ausentes1 = int(input(("Indique la cantidad de ausentes: ")))
        porcPresentes = float((presentes * 100) / totalAlumnos)
        print("Hay %{} de alumnos presentes en el curso 1".format(porcPresentes))
    elif (curso == 3):
        totalAlumnos = int(input(("Indique el total de alumnos del curso: ")))
        presentes = int(input(("Indique cantidad de alumnos presentes: ")))
        ausentes2 = int(input(("Indique la cantidad de ausentes: ")))
        porcPresentes = float((presentes * 100) / totalAlumnos)
        print("Hay %{} de alumnos presentes en el curso 2".format(porcPresentes))
    elif (curso == 4):
        totalAlumnos = int(input(("Indique el total de alumnos del curso: ")))
        presentes = int(input(("Indique cantidad de alumnos presentes: ")))
        ausentes3 = int(input(("Indique la cantidad de ausentes: ")))
        porcPresentes = float((presentes * 100) / totalAlumnos)
        print("Hay %{} de alumnos presentes en el curso 3".format(porcPresentes))
    elif (curso == 5):
        totalAlumnos = int(input(("Indique el total de alumnos del curso: ")))
        presentes = int(input(("Indique cantidad de alumnos presentes: ")))
        ausentes4 = int(input(("Indique la cantidad de ausentes: ")))
        porcPresentes = float((presentes * 100) / totalAlumnos)
        print("Hay %{} de alumnos presentes en el curso 4".format(porcPresentes))
    else:
        totalAlumnos = int(input(("Indique el total de alumnos del curso: ")))
        presentes = int(input(("Indique cantidad de alumnos presentes: ")))
        ausentes5 = int(input(("Indique la cantidad de ausentes: ")))
        porcPresentes = float((presentes * 100) / totalAlumnos)
        print("Hay %{} de alumnos presentes  en el curso 5".format(porcPresentes))
ausentesTotal = ausentes1 + ausentes2 + ausentes3 + ausentes4 + ausentes5
print("Hay un total de {} ausentes en el colegio".format(ausentesTotal))
if (ausentes1 > ausentes2 and ausentes1 > ausentes3 and ausentes1 > ausentes4 and ausentes1 > ausentes5):
    print("El curso 1 tiene la mayor cantidad de ausentes.")
elif (ausentes2 > ausentes3 and ausentes2 > ausentes4 and ausentes2 > ausentes5):
    print("El curso 2 tiene la mayor cantidad de ausentes.")
elif (ausentes3 > ausentes4 and ausentes3 > ausentes5):
    print("El curso 3 tiene la mayor cantidad de ausentes.")
elif (ausentes4 > ausentes5):
    print("El curso 4 tiene la mayor cantidad de ausentes.")
else:
    print("El curso 5 tiene la mayor cantidad de ausentes.")