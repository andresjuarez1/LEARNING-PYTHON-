print("Programa de calificaciones de alumnos")

nota_alumno=input("INTRODUCE LA NOTA QUE SACASTE: S")

def evaluacion (nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))