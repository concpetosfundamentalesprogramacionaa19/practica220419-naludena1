""""
archivo: Problema1
Problema1 en python
autor: naludena1
"""
# entrada de datos
horas = input("Ingrese el numero de horas trabajadas")
costoHoras = input("Ingrese el costo por hora")

# calculo del valor mensual y descuento
sueldoMensual = float(horas) * float(costoHoras)
desc = float(sueldoMensual) * 0.10
valorPagar = float(sueldoMensual) - float(desc)

# salida de datos
print ("El valor mensual a pagar es: %.2f\tEl descuento es: %.2f " % (valorPagar, desc))