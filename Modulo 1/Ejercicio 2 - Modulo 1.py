#2. Calcular el importe que debe pagar una persona compra una heladera
#de pesos X y por pagar en efectivo le hacen el 10% de descuento ¿Cuánto
#abona?

precio = float((input("Ingrese el valor de la heladera: $")))
descuento = (precio * 0.10)
precio_final = (precio - descuento)
print("Usted abona: $" + str(precio_final))