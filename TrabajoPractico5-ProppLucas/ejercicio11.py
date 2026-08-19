estudiantes = ["santiago","manuel","lautaro","jose","lucas","sandra","ciro","maximiliano","sara","sofia"]
print(estudiantes)
nombre_buscar = input("ingrese nombre a buscar: ")
if nombre_buscar in estudiantes:
    pos_nombre = estudiantes.index(nombre_buscar)
    print(f"Nombre encontrado en la posicion {pos_nombre+1}")
else:
    print("Nombre no encontrado")

    

