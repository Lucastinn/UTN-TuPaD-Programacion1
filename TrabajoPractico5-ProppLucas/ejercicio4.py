datos = [1,3,5,3,7,1,9,5,3]
print(datos)
datos_new = []
for dato in datos:
    if(datos_new.count(dato)<1 ):
        datos_new.append(dato)
print("Lista actualizada: \n")
print(datos_new)