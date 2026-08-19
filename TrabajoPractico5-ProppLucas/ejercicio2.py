productos = []
for i in range(4):
    print(f"producto {i+1}: ")
    producto = input("Ingrese producto: ")
    productos.append(producto)
print(sorted(productos))
producto_x = input("Que producto desea eliminar?: ")
productos.remove(producto_x)
print(sorted(productos))
