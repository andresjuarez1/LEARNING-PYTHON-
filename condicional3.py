# edad=-7

# if 0<edad<100:
#     print("Edad es correcta pa")
# else:
#     print("Edad incorrecta")

salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario del presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario del presidente: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("Salario del presidente: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salario del presidente: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo en orden pa")
    print(str (salario_administrativo) + " " +  str(salario_director) + " " + str(salario_jefe_area) + " " + str(salario_presidente))
else:
    print("No sabes pagar, vuelve a hacer TODO BIEN")
