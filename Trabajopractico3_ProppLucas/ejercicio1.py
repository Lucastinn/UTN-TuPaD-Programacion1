nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre = input("Error!, Ingrese su nombre (solo letras, no puede estar vacío): ")

cant_str = input("Ingrese cantidad de productos: ")
while not cant_str.isdigit() or int(cant_str) <= 0:
    cant_str = input("Error!, Ingrese cantidad de productos (entero positivo mayor a 0): ")
cant = int(cant_str)

totalSinDescuento = 0
totalConDescuento = 0
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant}")

for i in range(cant):
    precio_str = input(f"Ingrese precio del producto {i+1}: ")
    while not precio_str.isdigit():
        precio_str = input("Error!, Ingrese un precio válido (número entero): ")
    precio = int(precio_str)

    tieneDescuento = input("Tiene descuento? (S/N): ")
    while tieneDescuento.upper() != "S" and tieneDescuento.upper() != "N":
        tieneDescuento = input("Error, tiene descuento? (S/N): ")

    print(f"Producto {i+1} - Precio: {precio} Descuento (S/N): {tieneDescuento}")

    totalSinDescuento += precio
    if tieneDescuento.upper() == "S":
        descuento = precio * 0.10
        precioFinal = precio - descuento
    else:
        precioFinal = precio
    totalConDescuento += precioFinal

ahorro = totalSinDescuento - totalConDescuento
promedio = totalConDescuento / cant

print(f"Total sin descuentos: ${totalSinDescuento}")
print(f"Total con descuentos: ${totalConDescuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")