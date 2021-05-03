#6. Ingresar las edades de dos personas. Si una de ellas es mayor de edad
#y la otra menor de edad, calcular y mostrar su promedio. En caso contrario
#mostrar las dos edades.

persona1 = int(input("Ingrese la edad de la primera persona: "))
persona2 = int(input("Ingrese la edad de la segunda persona: "))
if (persona1 > 18 and persona2 < 18):
    edad_promedio = (persona1 + persona2) / 2
    print("El promedio de edad es {}".format(edad_promedio))
elif (persona2 > 18 and persona1 < 18):
    edad_promedio = (persona1 + persona2) / 2
    print("El promedio de edad es {}".format(edad_promedio))
else:
    print("La edad de la primera persona es {} y la edad de la segunda persona es {}".format(persona1,persona2))