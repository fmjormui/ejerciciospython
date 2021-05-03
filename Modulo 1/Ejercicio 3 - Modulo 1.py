#3. Hallar la longitud de la hipotenusa de un triángulo dada la medida de
#sus catetos

cateto_1 = float(input("Ingrese el valor de su catero: "))
cateto_2 = float(input("Ingrese el valor de su segundo cateto: "))
hipotenusa = ((cateto_1 ** 2) + (cateto_2 ** 2)) ** 0.5
print ("El valor de la hipotenusa es: " + str(hipotenusa))