import random

lista = []
for i in range(15):
    numero = random.randint(1, 100)
    lista.append(numero)
print(f"lista: {lista}\n")

lista_par = []
lista_impar = []
for numero in lista :
    if(numero % 2 == 0):
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f"cantidad lista par: {len(lista_par)}\n")
print(f"cantidad lista impar: {len(lista_impar)}\n")



