usuarioCorrecto = "alumno"
claveCorrecta = "python123"

band = 0
for i in range(3):
    usuario = input("ingrese nombre de usuario: ")
    clave = input("ingrese su clave: ")
    if usuario==usuarioCorrecto and clave==claveCorrecta:
        print("Usuario y clave correctas!\n")
        band = 1
        break
    else:
        print(f"ERROR! Credenciales invalidas \nIntento {i+1}/3\n")

if(band == 0):
    print("CUENTA BLOQUEADA")
else:
    print("1) Estado \n2) Cambiar clave \n3) Mensaje motivacional \n4) Salir \n")
    opc = input("Opcion (1-4): ")
    while(not opc.isdigit() or int(opc)<1 or int(opc)>4):
        opc = input("ERROR! , ingrese una opcion valida (1-4): ")
    while(int(opc)!=4):
        while(not opc.isdigit() or int(opc)<1 or int(opc)>4):
            opc = input("ERROR! , ingrese una opcion valida (1-4): ")
        if(int(opc) == 1):
            print("Inscripto \n")
        elif(int(opc) == 2):
            clave = input("Ingrese su nueva clave (minimo 6 caracteres): ")
            confirmacionClave = input("Ingrese nuevamente su clave para confirmar: ")
            if(clave==confirmacionClave and len(clave)>=6):
                print("Clave actualizada con exito\n")
            else:
                print("Confirmacion rechazada\n")
        elif (int(opc)==3):
            print("«El secreto de salir adelante es empezar.» — Mark Twain\n")
        print("1) Estado \n2) Cambiar clave \n3) Mensaje motivacional \n4) Salir \n")
        opc = input("Opcion (1-4): ")
        while(not opc.isdigit() or int(opc)<1 or int(opc)>4):
            opc = input("ERROR! , ingrese una opcion valida (1-4): ")
