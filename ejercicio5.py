"""
Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos.

"""
redes = int(input("Digite la cantidad de almunos de redes: "))
contabilidad = int(input("Digite la cantidad de almunos de contabilidad: "))
diseño = int(input("Digite la cantidad de almunos de diseño: "))

total = redes + contabilidad + diseño

porRedes = round((redes / total) * 100,1)
porContabilidad =round( (contabilidad / total) * 100, 1)
pordiseño = round((diseño / total) * 100,1)

print(f'Los porcentajes son: \n redes: {porRedes}% \n contabilidad: {porContabilidad}% \n diseño: {pordiseño}%')