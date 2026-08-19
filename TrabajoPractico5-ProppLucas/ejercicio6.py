lista = [1,2,3,4,5,6,7]
print(lista)
aux = lista[-1]
for i in range(len(lista)-1, 0,-1):
    lista[i] = lista[i-1]
lista[0] = aux
print("Lista actualizada")
print(lista)


