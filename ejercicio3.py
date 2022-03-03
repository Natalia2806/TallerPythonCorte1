"""
Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.
"""

sueldoBase = float(input("Ingrese el sueldo del vendedor: "))
ventas = float(input("Ingrese las ventas del mes: "))

extra = (ventas * 0.15) + ventas

total = sueldoBase + extra

print(f'El valor ganado por comision es : {extra:,} \n El valor total a pagar es : {total:,}')