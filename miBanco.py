estrato  = input("Ingrese el estrato de la persona: ")
estrato = int(estrato)

valor_deuda = input("Por favor ingresa el valor de la deuda: ")    # Aca estamos definiendo una variable
valor_deuda = float(valor_deuda)


interes = 0

if (estrato < 5):
    interes = 5
elif(estrato <= 7):
    interes = 5.5
else:
    interes = 6

porcentaje_calculado = valor_deuda*(1 + (interes/100))

print("El valor de la deuda es $", valor_deuda)
print("El estrato es", estrato)
print("El valor del interes es", interes, "%")
print("Resultado $",porcentaje_calculado)    # Aca estamos imprimiendo el valor de el porcentaje calculado
