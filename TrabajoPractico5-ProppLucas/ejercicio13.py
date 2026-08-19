puntajes = [450, 1200, 875, 990, 300, 1500, 640]

mayor = 0
menor = 9999999
for puntos in puntajes:
    if puntos>mayor:
        mayor = puntos
    if puntos<menor:
        menor=puntos
print(f"Puntaje mas alto: {mayor}")
print(f"Puntaje mas bajo: {menor}\n")

print("Ranking")
ranking = sorted(puntajes,reverse=True)
for ptos in ranking:
    print(ptos)
print("\n")

pos_990 = ranking.index(990)
print(f"990 esta en la posicion{pos_990+1} del ranking")

