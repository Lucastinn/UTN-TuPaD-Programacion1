#Ta-te-ti
tablero = []
for i in range(3):
    for j in range(3):
        tablero.append("-")

for i in range(3):
    print(tablero[i*3],tablero[i*3+1],tablero[i*3+2])

for i in range(9):
    if(i%2==0):
        print("Turno jugador 1")
    else:
        print("Turno jugador 2")
    pos = (input("Ingrese fila y columna (ej: 1 2): "))
    while(not(pos[0].isdigit() and pos[2].isdigit() and pos[1]==" " and int(pos[0])>=1 and int(pos[0])<=3 and int(pos[2])>=1 and int(pos[2])<=3)):
        print("Posición inválida, ingrese nuevamente")
        pos = (input("Ingrese fila y columna (ej: 1 2): "))
