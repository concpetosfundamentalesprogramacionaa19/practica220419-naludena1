""""
archivo: Problema2
Problema2 en python
autor: naludena1
"""
# entrada de datos
x = input("Ingrese la primera variable")
y = input("Ingrese la segunda variable")
z = input("Ingrese la tercera variable")

# conversion de datos
variablex = float (x)
variabley = float (y)
variablez = float (z)

# calculo de datos
m = float ((variablex + (variabley/variablez)) / (variablex - (variabley/variablez)))

# salida de datos
print ("El valor de m, en base de las variables: \nx= %.1f \n\ty= %.1f \n\t\tz= %.1f \nda como resultado: \n\t\tm=%.1f" % (variablex, variabley, variablez, m))
