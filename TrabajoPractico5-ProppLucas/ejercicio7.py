temperaturas = []
for i in range(7):
    print(f"dia {i+1}:")
    temp_min_max = []
    for j in range(2):
        if(j==0):
            temp = int(input("Ingrese temperatura minima: "))
            temp_min_max.append(temp)
        else:
            temp = int(input("Ingrese temperatura maxima: "))
            temp_min_max.append(temp)
    temperaturas.append(temp_min_max)
print(temperaturas)

suma_min = 0
suma_max = 0
for i in range(7):
    suma_min += temperaturas[i][0]
for i in range(7):
    suma_max += temperaturas[i][1]
prom_min = suma_min/7
prom_max = suma_max/7

mayor = 0
indice_dia = 0
for i in range(len(temperaturas)):
    if(temperaturas[i][1] - temperaturas[i][0])>mayor :
        mayor = (temperaturas[i][1] - temperaturas[i][0])
        indice_dia = i+1

print(f"El promedio de las minimas es: {prom_min:.2f}ºC\n")
print(f"El promedio de las maximas es: {prom_max:.2f}ºC\n")
print(f"dia de mas amplitud termica: {indice_dia}")



