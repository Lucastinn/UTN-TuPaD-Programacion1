energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False

nombre_agente = input("Ingrese nombre del agente: ")
while(not nombre_agente.isalpha()):
    print("ERROR!, Nombre invalido\n")
    nombre_agente = input("Ingrese nombre del agente: ")
while(energia>0 and tiempo>0 and cerraduras_abiertas<3 and not bloqueado):
    print(f"ESTADO\nEnergia: {energia}\nTiempo: {tiempo}\nCerraduras abiertas: {cerraduras_abiertas}\n")
    print("1) Forzar cerradura\n2) Hackear panel\n3) Descansar\n")
    opc = input("Opcion... : ")
    while(not opc.isdigit() or int(opc)<1 or int(opc)>3):
        print("ERROR! Opcion invalida\n")
        opc = input("Opcion... : ")
    if(int(opc)==1):
        energia-=20
        tiempo-=2
        forzar_seguidas+=1
        if(forzar_seguidas==3):
            alarma = True
            print("Cerradura trabada\n")
        if(energia<40 and not alarma):
            print("¡Riesgo de alarma!\n")
            num = input("Elige un numero (1-3): ")
            while(not num.isdigit() or int(num)<1 or int(num)>3):
                print("ERROR! Numero invalido\n")
                num = input("Elige un numero (1-3): ")
            if(int(num)==3):
                alarma = True     
        if(not alarma):
            cerraduras_abiertas+=1
            print("Cerradura abierta con exito!")
    elif(int(opc)==2):
        energia-=10
        tiempo-=3
        forzar_seguidas = 0
        for i in range(4):
            codigo_parcial += "X"
            print(f"Paso {i+1}/4 - Codigo: {codigo_parcial}\n")
        if(len(codigo_parcial)>=8 and cerraduras_abiertas<3):
            cerraduras_abiertas+=1
            print("Cerradura abierta con exito\n")
    elif(int(opc)==3):
        forzar_seguidas = 0
        if(energia<100):
            energia+=15
            if(energia>=100):
                energia = 100
        tiempo -=1
        if(alarma):
            energia-=10
    if(alarma and tiempo<=3):
        bloqueado = True
        print("Sistema bloqueado")
print(f"Agente: {nombre_agente}\n")
if(cerraduras_abiertas==3):
    print("VICTORIA")
elif(energia<=0 or tiempo<=0):
    print("DERROTA")
elif(bloqueado):
    print("DERROTA (BLOQUEO)")
        
