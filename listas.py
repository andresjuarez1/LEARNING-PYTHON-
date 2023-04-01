# nombreLista=["Maria", "pepe", "marta", "antonio"]
# print(nombreLista[:]) 

# nombreLista=["Maria", "pepe", "marta", "antonio"]
# print(nombreLista[2])

# nombreLista=["Maria", "pepe", "marta", "antonio"]
# print(nombreLista[0:2]) #para acceder hasta una determinada posicion a otra 


nombreLista=["Maria", "pepe", "marta", "antonio"]

# nombreLista.append("Sandra") #para agregar un elemento al final de la lista
# nombreLista.insert(2, "Luis") #para agregar enmedio de la lista, el primer valor es para seleccionar su posicion
nombreLista.extend(["Sandra", "Ana", "Lucia"]) #para agregar varios elementos

# print("kaka" in nombreLista) para saber si el elemento existe dentro de la lista 
# print(nombreLista.index("Ana")) #para saber la posicion del elemento en la lista


listaVariada=["Maria", 5, True, 78.35]
listaVariada.extend(["Sandra", "Ana", "Lucia"])

# listaVariada.remove("Ana") para eliminar un elemento de la lista
# listaVariada.pop() elimina el ultimo elemento de una lista

# print(listaVariada[:])


miLista=["maria", 5, True, 78.35]
miLista2=["Sandra", "Lucia"] * 3 #el "* 3" es para repetir una lista 3 veces

miLista3=miLista+miLista2

print(miLista3[:])