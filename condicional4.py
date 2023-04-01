# print("Programa de becas año 2023")

# distancia_escuela=int(input("Introduce la distancia a la que esta tu escuela en km: "))
# print(distancia_escuela)

# numero_hermanos=int(input("Introduce el numero de hermanos que tienes: "))
# print(numero_hermanos)

# salario=int(input("Introduce el salario anual de tu papa: "))
# print(salario)

# if distancia_escuela>40 and numero_hermanos>2 or salario<=2000:
#     print("Todo bien pa, estas becado")
# else:
#     print("No tienes derecho a beca")

print("Carga de materias pa")
print("Materias optativas: estructura de datos - base de datos - poo")
opcion=input("Escribe la materia escogida: ")

materia=opcion.lower() #esto es para convertir todo lo ingresado a minusculas y para convertir a mayusculas es .upper()

if materia in ("estructura de datos ", "base de datos", "poo"):
    print("Materia escogida: "  + materia)
else:
    print("La materia no existe")