""""
archivo: demo2.py
Ejemplo de lenguaje Python
autor: naludena1
"""
import sys

nombre_archivo = sys.argv[0] # nombre del archivo
valor1 = sys.argv[1] # variable1
valor2 = sys.argv[2] # variable2

suma = int(valor1) + int(valor2)  # Suma de variables #Convertir cadenas en enteros

print("La suma es: %s" % suma) # Impresión del cálculo
