nombre = input("Ingrese su nombre: ")
while(not nombre.isalpha()):
    print("ERROR! Nombre invalido")
    nombre = input("Ingrese su nombre: ")

lunes1=""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""

print(f"1) Reservar turno \n2) Cancelar turno (Por nombre)\n3) Ver agenda del dia\n4) Ver resumen general\n5) Cerrar sistema\n")
opc = input("Opcion... : ")
while(not opc.isdigit() or int(opc)<1 or int(opc)>5):
    print("ERROR! Opcion invalida\n")
    opc = input("Opcion... : ")
while(int(opc)!=5):
    print(f"1) Reservar turno \n2) Cancelar turno (Por nombre)\n3) Ver agenda del dia\n4) Ver resumen general\n5) Cerrar sistema\n")
    while(not opc.isdigit() or int(opc)<1 or int(opc)>5):
        print("ERROR! Opcion invalida\n")
        opc = input("Opcion... :")
    if(int(opc)==1):
        print("1: Lunes , 2: Martes\n")
        opcDia = input("Dia... : ")
        while(not opcDia.isdigit() or int(opcDia)<1 or int(opcDia)>2):
            print("ERROR! Dia invalido\n")
            print("1: Lunes , 2: Martes\n")
            opcDia = input("Dia... : ")
        nombre = input("Ingrese su nombre: ")
        while(not nombre.isalpha()):
            print("ERROR! Nombre invalido\n")
            nombre = input("Ingrese su nombre: ")
        if(int(opcDia)==1): #Lunes
            if(nombre==lunes1 or nombre==lunes2 or nombre==lunes3 or nombre==lunes4):
                print("Ya existe una reserva a su nombre para el dia lunes")
            else:
                if(lunes1==""):
                    lunes1 = nombre
                    print(f"Turno reservado {nombre}: Lunes, Turno1\n")
                elif(lunes2==""):
                    lunes2 = nombre
                    print(f"Turno reservado {nombre}: Lunes, Turno2\n")
                elif(lunes3==""):
                    lunes3=nombre
                    print(f"Turno reservado {nombre}: Lunes, Turno3\n")
                elif(lunes4==""):
                    lunes4=nombre
                    print(f"Turno reservado {nombre}: Lunes, Turno4\n")
                else:
                    print("No hay turnos disponibles el lunes\n")
        else: #Martes
            if(nombre==martes1 or nombre==martes2 or nombre==martes3):
                print("Ya existe una reserva a su nombre para el dia martes")
            else:
                if(martes1==""):
                    martes1 = nombre
                    print(f"Turno reservado {nombre}: Martes, Turno1\n")
                elif(martes2==""):
                    martes2 = nombre
                    print(f"Turno reservado {nombre}: Martes, Turno2\n")
                elif(martes3==""):
                    martes3=nombre
                    print(f"Turno reservado {nombre}: Martes, Turno3\n")
                else:
                    print("No hay turnos disponibles el martes\n")
    elif(int(opc)==2):
        print("1: Lunes , 2: Martes\n")
        opcDia = input("Dia... : ")
        while(not opcDia.isdigit() or int(opcDia)<1 or int(opcDia)>2):
            print("ERROR! Dia invalido\n")
            print("1: Lunes , 2: Martes\n")
            opcDia = input("Dia... : ")
        nombre = input("Ingrese su nombre: ")
        while(not nombre.isalpha()):
            print("ERROR! Nombre invalido\n")
            nombre = input("Ingrese su nombre: ")
        if(int(opcDia)==1): #Lunes
            if(lunes1==nombre):
                lunes1=""
                print(f"Turno cancelado {nombre}: Lunes, Turno1")
            elif(lunes2==nombre):
                lunes2=""
                print(f"Turno cancelado {nombre}: Lunes, Turno2")
            elif(lunes3==nombre):
                lunes3=""
                print(f"Turno cancelado {nombre}: Lunes, Turno3")
            elif(lunes4==nombre):
                lunes4=""
                print(f"Turno cancelado {nombre}: Lunes, Turno4")
            else:
                print("No existia un turno reservado a tu nombre para el dia lunes\n")
        else: #Martes
            if(martes1==nombre):
                martes1=""
                print(f"Turno cancelado {nombre}: Martes, Turno1")
            elif(martes2==nombre):
                martes2=""
                print(f"Turno cancelado {nombre}: Martes, Turno2")
            elif(martes3==nombre):
                martes3=""
                print(f"Turno cancelado {nombre}: Martes, Turno3")
            else:
                print("No existia un turno reservado a tu nombre para el dia martes\n")
    elif(int(opc)==3):
        print("1: Lunes , 2: Martes\n")
        opcDia = input("Dia... : ")
        while(not opcDia.isdigit() or int(opcDia)<1 or int(opcDia)>2):
            print("ERROR! Dia invalido\n")
            print("1: Lunes , 2: Martes\n")
            opcDia = input("Dia... : ")
        if(int(opcDia)==1): #Lunes
            print("Lunes\n")
            if(lunes1==""):
                print("Turno1: (Libre)")
            else:
                print(f"Turno1: {lunes1}")
            if(lunes2==""):
                print("Turno2: (Libre)")
            else:
                print(f"Turno2: {lunes2}")
            if(lunes3==""):
                print("Turno3: (Libre)")
            else:
                print(f"Turno3: {lunes3}")
            if(lunes4==""):
                print("Turno4: (Libre)\n")
            else:
                print(f"Turno4: {lunes4}\n")
        else: #Martes
            print("Martes")
            if(martes1==""):
                print("Turno1: (Libre)")
            else:
                print(f"Turno1: {martes1}")
            if(martes2==""):
                print("Turno2: (Libre)")
            else:
                print(f"Turno2: {martes2}")
            if(martes3==""):
                print("Turno3: (Libre)\n")
            else:
                print(f"Turno3: {martes3}\n")
    elif(int(opc)==4):
        ocupadosLunes, ocupadosMartes = 0,0
        libresLunes, libresMartes = 0,0
        if(lunes1!=""): #Lunes
            ocupadosLunes+=1
        else:
            libresLunes+=1    
        if(lunes2!=""):
            ocupadosLunes+=1
        else:
            libresLunes+=1    
        if(lunes3!=""):
            ocupadosLunes+=1    
        else:
            libresLunes+=1    
        if(lunes4!=""):
            ocupadosLunes+=1    
        else:
            libresLunes+=1
        if(martes1!=""): #Martes
            ocupadosMartes+=1
        else:
            libresMartes+=1    
        if(martes2!=""):
            ocupadosMartes+=1
        else:
            libresMartes+=1    
        if(martes3!=""):
            ocupadosMartes+=1    
        else:
            libresMartes+=1
        print(f"Turnos ocupados\nLunes: {ocupadosLunes}\nMartes: {ocupadosMartes}\n")
        print(f"Turnos libres\nLunes: {libresLunes}\nMartes: {libresMartes}\n")
        if(ocupadosLunes>ocupadosMartes):
            print("El dia con mas turnos es: Lunes\n")
        elif(ocupadosMartes>ocupadosLunes):
            print("El dia con mas turnos es: Martes\n")
        else: 
            print("Ambos dias tienen los mismos turnos\n")
    print(f"1) Reservar turno \n2) Cancelar turno (Por nombre)\n3) Ver agenda del dia\n4) Ver resumen general\n5) Cerrar sistema\n")
    opc = input("Opcion... : ")
    while(not opc.isdigit() or int(opc)<1 or int(opc)>5):
        print("ERROR! Opcion invalida\n")
        opc = input("Opcion... : ")