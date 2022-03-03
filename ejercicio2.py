"""
Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.
"""

inversion1 = float(input("Ingrese el dinero de la persona 1: "))
inversion2 = float(input("Ingrese el dinero de la persona 2: "))
inversion3 = float(input("Ingrese el dinero de la persona 3: "))

total = inversion1 + inversion2 + inversion3

porcen1 = (inversion1 / total)*100
porcen2 = (inversion2 / total)*100
porcen3 = (inversion3 / total)*100

print(f'Los porcentajes son: \n Persona 1: {porcen1}% \n Persona 2: {porcen2}% \n persona 3: {porcen3}%')