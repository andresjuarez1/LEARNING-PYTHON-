# for letra in "Python":

#     if letra=="h":
#         continue 

#     print("Viendo la letra: " + letra)


# nombre="hola soy andres"
# contador=0

# for i in nombre:
#     if i==" ":
#         continue
#     contador+=1

# print(contador)


email=input("Introduce tu email, vos chito: ")

for i in email:
    if i=="@":
        arroba=True
        print("Todo bien con tu correo")
        break

else:
    arroba=False
    print("Verifica tu correo")

