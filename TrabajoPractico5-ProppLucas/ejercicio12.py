lista = []
for i in range(8):
    print(f"Posicion {i+1}: ")
    nro = int(input("nro: "))
    lista.append(nro)

print(f"Lista original: {lista}")
lista_men_may = sorted(lista)
print(f"lista menor a mayor: {lista_men_may}")
lista_may_men = sorted(lista, reverse=True)
print(f"lista mayor a menor: {lista_may_men}")