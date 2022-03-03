"""
Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.
"""

taller1 =  float(input("Ingrese la califiacion del taller 1: "))
taller2 =  float(input("Ingrese la califiacion del taller 2: "))
taller3 =  float(input("Ingrese la califiacion del taller 3: "))

examen = float(input("Calificacion de examen: "))

proyecto = float(input("Proyecto final: "))

PromedioTalleres = (taller1 + taller2 + taller3) / 3
porcentajeTalleres = (PromedioTalleres * 0.50)

porcentExamen = (examen * 0.30)

porcenProyecto = (proyecto * 0.20)

total = porcentajeTalleres + porcentExamen +porcenProyecto


print(f'Calificacion final es : {round(total,1)}')