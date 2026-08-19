ventas = []
for i in range(7):
    print(f"DIA {i+1}: ")
    productos = []
    for i in range(4):
        print(f"producto: {i+1}:  ")
        venta = int(input("ingrese cantidad de ventas: "))
        productos.append(venta)
    ventas.append(productos)
    print("\n")


for i in range(len(ventas)):
    for j in range(len(productos)):
        print(f"{ventas[i][j]}")
    print("\n")

for j in range(len(productos)):
    suma = 0
    for i in range(len(ventas)):
        suma+=ventas[i][j]
    print(f"Total producto {j+1}: {suma} ")

indice_dia_mayor = -1
mayor = 0
for i in range(len(ventas)):
    suma = 0
    for j in range(len(productos)):
        suma+=ventas[i][j]
    if suma > mayor:
        mayor = suma
        indice_dia_mayor = i+1
print(f"Dia de mas ventas: {indice_dia_mayor}")

indice_producto_mayor = -1
mayor = 0
for i in range(len(productos)):
    suma = 0
    for j in range(len(ventas)):
        suma+=ventas[j][i]
    if(suma > mayor):
        mayor = suma
        indice_producto_mayor = i+1
print(f"Producto mas vendido: {indice_producto_mayor}")        



