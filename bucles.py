# for i in ["primavera", "verano", "otoño", "invierno"]:
#     print(i)

# for i in ["Pildoras", "Informaticas", 3]:
#     print("hola", end=" ")

# email=False
# IngresarEmail=input("Agrega tu email ")

# for i in IngresarEmail:
#     if(i=="@"):
#         email=True

# if email==True:
#     print("Email correcto pa")
# else:
#     print("pusiste mal tu correo pa")


contadorArroba=0
contadorPunto=0
IngresarEmail=input("Agrega tu email ")

for caracter in IngresarEmail:
    if caracter == "@":
        contadorArroba += 1
    elif caracter==".":
        contadorPunto += 1

if contadorArroba ==1 and contadorPunto ==1:
    print("Email correcto pa")
else:
    print("pusiste mal tu correo pa")