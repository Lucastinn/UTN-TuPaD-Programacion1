lista = ["marcos", "pedro", "juan", "lucas", "ignacio", "franco", "gonzalo", "nahuel"]
print(lista)
opc = input("1) agregar nuevo estudiante\n2) eliminar estudiante existente\nopcion... : ")
while(not opc.isdigit() or int(opc)<1 or int(opc)>2):
    print("Error! opcion invalida\n")
    opc = input("1) agregar nuevo estudiante\n2) eliminar estudiante existente\nopcion... : ")

if(int(opc)==1):
    nombre = input("Ingrese nombre: ")
    while(not nombre.isalpha()):
        print("Error! Nombre invalido")
        nombre = input("Ingrese nombre: ")
    lista.append(nombre)
else:
    nombre = input("Ingrese nombre: ")
    while(not nombre.isalpha()):
        print("Error! Nombre invalido")
        nombre = input("Ingrese nombre: ")
    lista.remove(nombre)

print("Lista actualizada: \n")
print(lista)