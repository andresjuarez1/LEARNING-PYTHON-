import math

# i=i

# while i<=10:
#     print("Ejecucion " + str(i))
#     i=i+1

# print("Termino la ejecucion")


# edad=int(input("Introduce tu edad: "))

# while edad<5 or edad>100:
#     print("Tu edad esta mal chito, intentalo otra vez")
#     edad=int(input("Introduce tu edad: "))

# print("Gracias por colaborar chunco, pasale")
# print("Edad del chito: " + str(edad))


print("Programa de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
    print("No se puede hayar esa raiz chito")

    if intentos==2:
        print("Has hecho muchos intentos vos, andate a mimir")
        break;

    numero=int(input("Introduce un numero: "))
    if numero<0:
        intentos= intentos +1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada del numero es: " + str(numero) + "es " + str(solucion))