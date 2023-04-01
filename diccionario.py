miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Mexico":"CDMX", "España":"Madrid"}
miDiccionario["Italia"]="Lisboa" #para agregar un dato al diccionario
miDiccionario["Italia"]="Roma" #para corregir un dato en el diccionario, python lee de arriba hacia abajo
del miDiccionario["Mexico"] #eliminar un dato

#print(miDiccionario["Francia"])
# print(miDiccionario)


miDiccionario2={"Alemania":"Berlin", 23:"Jordan", "Messi":10}
# print(miDiccionario2)


miTupla=["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario3={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}
# print(miDiccionario3["Francia"])
print(miDiccionario3.keys()) #te da las claves del diccionario