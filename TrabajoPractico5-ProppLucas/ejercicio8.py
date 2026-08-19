estudiantes = []
for i in range(5):
    print(f"Estudiante {i+1}: ")
    materia = []
    for j in range(3):
        print(f"Materia {j+1}: ")
        nota = int(input("nota: "))
        materia.append(nota)
    estudiantes.append(materia)
    print("\n")

for i in range(len(estudiantes)):
    suma = 0
    for j in range(len(materia)):
        suma += estudiantes[i][j]
    print(f"Promedio estudiante {i+1}: {suma/len(materia):.2f}")
print("\n")
for j in range(len(materia)):
    suma = 0
    for i in range(len(estudiantes)):
        suma+=estudiantes[i][j]
    print(f"Promedio materia {j+1}: {suma/len(estudiantes):.2f}")
    