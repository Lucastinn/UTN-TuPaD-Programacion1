nombre_gladiador = input("ingrese nombre del gladiador: ")
while(not nombre_gladiador.isalpha()):
    print("ERROR! ingrese un nombre valido\n")
    nombre_gladiador = input("ingrese nombre del gladiador: ")
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_base = 15
daño_base_enemigo = 12
turno_gladiador = True
while(vida_gladiador>0 and vida_enemigo>0):
    while(turno_gladiador):
        print(f"{nombre_gladiador} (HP:{vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}\n")
        print("1. Ataque pesado\n2. Rafaga veloz\n3.Curar\n")
        opc = input("opcion... : ")
        while(not opc.isdigit() or int(opc)<1 or int(opc)>3):
            print("ERROR! ingrese una opcion valida\n")
            opc = input("opcion... : ")
        if(int(opc)==1):
            if(vida_enemigo<20):
                vida_enemigo -= int(daño_base*1.5)
                print("Golpe critico!\n")
                print(f"¡Atacaste al enemigo por {daño_base*1.5} puntos de daño!")
            else:
                vida_enemigo-=daño_base
                print(f"¡Atacaste al enemigo por {daño_base} puntos de daño!")
        elif(int(opc)==2):
            print("¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo-=5
                print("Golpe conectado por 5 de daño")
        elif(int(opc)==3):
            if(pociones_vida>0):
                print("¡Te has curado!\n")
                vida_gladiador+=30
                pociones_vida-=1
                if(vida_gladiador>100):
                    vida_gladiador = 100
            else:
                print("¡No quedan pociones!\n")
        turno_gladiador = False
    while(not turno_gladiador and vida_enemigo>0):
        vida_gladiador-=12
        print("¡El enemigo contraataca por 12 puntos de daño!\n")
        turno_gladiador=True
if(vida_gladiador>0):
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")