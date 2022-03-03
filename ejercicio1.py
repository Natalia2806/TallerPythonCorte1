"""
1. Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación
"""

donacion = float(input("Digite el valor de la donacion: "))

administracion = (donacion * 0.35)

sistemas = (administracion * 0.25)

telecomunicaciones = (sistemas * 0.1)

contabilidad = donacion - (administracion + sistemas + telecomunicaciones)

print(f'La donacion fue de: ${donacion} \n Telecomunicaciones: ${telecomunicaciones} \n Sistemas: ${sistemas} \n Administracion: ${administracion} \n Contabilidad: ${contabilidad}')
